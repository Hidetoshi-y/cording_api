from types import SimpleNamespace
from flask import *

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
        #4桁だけの場合



def _convert_kanji(number):
    number = list(number)
    numbers = len(number)
    new_number = []

    """
    for i in range(numbers):
        new_number += convert_simple_kanji(number[i])#表示されている数字を漢数字に変換可能"""

    return new_number








@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/v1/number2kanji/<name>", methods=["GET", "POST"]) #数字漢数字変換
def number2kanjie(name):
    #name = int(name) - int(30)
    name = _convert_kanji(name)

    return render_template("number2kanji.html", name=name)
    #http://localhost:8888/v1/number2kanji/100


@app.route("/v1/kanji2number/<name>", methods=["GET", "POST"]) #漢数字数字変換
def kanji2number(name):
    name = int(name) + int(30)
    return render_template("kanji2number.html", name=name)
    #http://localhost:8888/v1/kanji2number/100


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)