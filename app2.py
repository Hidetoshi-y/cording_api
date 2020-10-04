from types import SimpleNamespace
from flask import *
import re

app = Flask(__name__)



class Kansuuji():
    def __init__(self,text=""):
        #不正な文字列に対するバリデーションがあるとよい。
        self.kan=text


    def _convert_single_KAN(self,one):
        """chars={
        "壱":1,
        "弐":2,
        "参":3,
        "四":4,
        "五":5,
        "六":6,
        "七":7,
        "八":8,
        "九":9,
        "十":10,
        "百":100,
        "千":1000
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
        9:"九",
        10:"十",
        100:"百",
        1000:"千"
        }
        return chars.get(one,1)    #十三など、一のつかないものに対応するため、getで1を返させている。

    def _change_num_under1000(self,text):

        C=self._convert_single_KAN
        val=0

        kans=(    
            ("千",1000),
            ("百",100),
            ("十",10)
        )    #処理順を保つためディクショナリは回避。

        for kan,num in kans:
            pat="([二三四五六七八九])?{}(.*)".format(kan)
            matobj=re.match(pat,text)
            if matobj:
                val+=C(matobj.group(1))*num
                text=matobj.group(2)

        if text:    #一の位を処理
            val +=C(text)

        return val

    def _change_num_over1000(self,text):
        val=0
        C2=self._change_num_under1000

        kans=(
            ("兆",1000000000000),
            ("億",100000000),
            ("万",10000)
        )    

        for kan,num in kans:
            pat="([一二三四五六七八九十百千]+){}(.*)".format(kan)
            matobj=re.match(pat,text)
            if matobj:
                val+=C2(matobj.group(1))*num
                text=matobj.group(2)

        return text,val


    def get_arabic(self,text=None):
        text=text if text else self.kan    #インスタンス作成時に引数を与えなくても動くようにしてみた。（こういうのはよくない？？）
        text,val=self._change_num_over1000(text)
        return val+self._change_num_under1000(text)








@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/v1/number2kanji/<name>", methods=["GET", "POST"]) #数字漢数字変換
def number2kanjie(name):
    #name = int(name) - int(30)
    name = Kansuuji(name)

    return render_template("number2kanji.html", name=name)
    #http://localhost:8888/v1/number2kanji/100


@app.route("/v1/kanji2number/<name>", methods=["GET", "POST"]) #漢数字数字変換
def kanji2number(name):
    name = int(name) + int(30)
    return render_template("kanji2number.html", name=name)
    #http://localhost:8888/v1/kanji2number/100


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
