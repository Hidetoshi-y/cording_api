from types import SimpleNamespace
from typing import Pattern
from flask import *

import numpy as np

import re
import urllib.parse



app = Flask(__name__)



def convert_simple_kanji(number):
    number = int(number)

    chars= {
        0:"零",
        1:"壱",
        2:"弐",
        3:"参",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九"
    }
    return chars.get(number,1)

def under_1000(number):
    #桁数分だけ桁を入れて桁数の漢数字が０のときに両方を消す。

    #４桁分の処理をいれる配列
    new_number = []

    #獲得した文字列を配列で処理する
    number = list(number)
    
    #まず配列の数字を全て漢字に変換
    for i in range(len(number)):
        new_number.append(convert_simple_kanji(str(number[i])))

    for j in range(len(new_number)):

        if j == 3:
            new_number.insert(-5, "千")
        elif j == 2:
            new_number.insert(-3, "百")
        elif j == 1:
            new_number.insert(-1, "拾")
        else:
            pass
    
    #零の後ろの単位を消去するためのリスト作り
    ##零の位置を特定
    del_list = [i for i, x in enumerate(new_number) if x == '零']

    ##特定した零の位置から後ろの単位を削除
    del_add_list = []
    for k, l in enumerate(del_list):
        if l == 6:
            pass
        else:
            l += 1
            del_add_list.append(l)
    del_list = del_list + del_add_list

    #指定したインデックスを削除する関数
    dellist = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]
    new_number = dellist(new_number, del_list)

    return new_number

def input_number_division(name):
    """入力文字列を４桁に区切って拾百千を付け加えた後に兆万億を追加する。 """
    number = list(name)

    for i in range(16):
        if len(number) == 16:
            break
        else:
            number.insert(0, "0")

    number = np.array(number)

    number = number.reshape([-1,4])

    consert_list = []
    for i, j in enumerate(number):
        name = under_1000(j)

        consert_list += name

        if i == 0 and len(consert_list) >= 1:
            consert_list.append("兆")
        elif i == 1 and len(consert_list) >=1:
            consert_list.append("億")
        elif i == 2 and len(consert_list) >=1:
            consert_list.append("万")
    
    number = consert_list

    number = "".join(map(str, number))
    
    return number


def convert_simple_number(number): #漢字->数字
    #number = int(number)
    chars= {
        "零":0,
        "壱":1,
        "弐":2,
        "参":3,
        "四":4,
        "五":5,
        "六":6,
        "七":7,
        "八":8,
        "九":9,
        "拾":10,
        "百":100,
        "千":1000,
        "一":1,
        "万":10000,
        "億":100000000,
        "兆":1000000000000,
    }
    return chars.get(number,1)


def parse_kanji(name, list):

    all_list = []
    mini_list = name

    for i in list :#3回実行
        
        #print(f"区切り文字{i}, 区切り対象{mini_list}")
        short_list = re.split(i, mini_list)

        if len(short_list) < 2 :
            mini_list = short_list[0]
        else:
            #print("short_list ", short_list)

            all_list.append((short_list[0], i))
            mini_list = short_list[1]
        #print("mini_list",mini_list)
    
        

    if len(mini_list) > 0:
        all_list.append((mini_list, "一"))
        

    return all_list

def calc_all(name, big_unit, short_unit):
    name_2 = parse_kanji(name, big_unit)
    sum = 0

    for i in name_2:
        a = convert_simple_number(i[1])

        name_3 = parse_kanji(i[0], short_unit)
        z = 0

        for j in name_3:
            x = convert_simple_number(j[0])
            y = convert_simple_number(j[1])
            z += x * y

        sum += a *z

    return sum 






@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/v1/number2kanji/<name>", methods=["GET", "POST"]) #number2kanji

def number2kanjie(name):
    name = urllib.parse.unquote(name)


    return_html = ()

    if name == "0": #①入力時[0]のときに零を返す。
        name = "零"
        return_html = render_template("number2kanji.html", name=name)

    elif 1 <= int(name) and 10000000000000000 >= int(name): #②入力が[1]~[9999999999999999]の時　数字2漢数字　を実行する。
        name = input_number_division(name)
        return_html = render_template("number2kanji.html", name=name)

    else: #③入力されたエンドポイントが[0]~[9999999999999999]以外の時
        return_html = render_template("error.html", name=name)

    return return_html


@app.route("/v1/kanji2number/<name>", methods=["GET", "POST"]) #kanji2number

def kanji2number(name):
    name = urllib.parse.unquote(name)
    return_html = ()

    check_list = ["壱","弐","参","四","五","六","七","八","九","拾","百","千","万","億","兆"]

    if name == "零": #①入力時[零]のときに0を返す。
        name = "0"
        return_html = render_template("kanji2number.html", name=name)


    elif name.isalpha() and 31 >= len(list(name)): #②　31文字以下かつ漢数字でない場合
        checker_lsit = list(name)

        for i in range(len(name)): #指定されたリストに無い文字の場合
            if str(checker_lsit[i]) in check_list:
                pass
            else:
                return_html = render_template("error.html", name=name)

        """
        ここアラビア数字を数字に変換する関数を記述する。
        name = input_number_division(name)
        return_html = render_template("kanji2number.html", name=name)
        """
        big_unit = ["兆","億","万"]
        short_unit = ["千","百","拾"]
        #name = parse_kanji(name, big_unit)
        

        name = calc_all(name, big_unit, short_unit)


        return_html = render_template("kanji2number.html", name=name)


    else: #③入力されたエンドポイントが漢数字では無い　かつ　範囲外
        return_html = render_template("error.html", name=name)


    return return_html
    














if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5002, threaded=True)
