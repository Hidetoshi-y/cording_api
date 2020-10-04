from types import SimpleNamespace
from flask import *

app = Flask(__name__)

def convert_simple_kanji(number):

    
    if number == "0":
        number = "零"
    elif number == "1":
        number = "壱"
    elif number == "2":
        number = "弐"
    elif number == "3":
        number = "参"
    elif number == "4":
        number = "四"
    elif number == "5":
        number = "五"
    elif number == "6":
        number = "六"
    elif number == "7":
        number = "七"
    elif number == "8":
        number = "八"
    elif number == "9":
        number = "九"
    else:
        pass

    return number



def _convert_kanji(number):
    number = list(number)
    numbers = len(number)

    new_number = []


    for i in range(numbers):
        new_number += convert_simple_kanji(number[i])#表示されている数字を漢数字に変換可能

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
