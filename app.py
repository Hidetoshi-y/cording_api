from types import SimpleNamespace
from flask import *

import numpy as np

app = Flask(__name__)



def convert_simple_kanji(number):
    number = int(number)
    """
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
    }"""

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
    #最大で４つに別れる。
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

"""
input_number_division -> under_1000 -> convert_simple_kanji

n
"""





@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/v1/number2kanji/<name>", methods=["GET", "POST"]) #数字漢数字変換

def number2kanjie(name):
    #①入力が０の場合　②入力が指定範囲の場合 ③入力が指定範囲外の場合を用意　
    #name = under_1000(name)

    name = input_number_division(name)#②

    return render_template("number2kanji.html", name=name)
    #http://localhost:8888/v1/number2kanji/100


@app.route("/v1/kanji2number/<name>", methods=["GET", "POST"]) #漢数字数字変換
def kanji2number(name):
    name = int(name) + int(30)
    return render_template("kanji2number.html", name=name)
    #http://localhost:8888/v1/kanji2number/100


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
