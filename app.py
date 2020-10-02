from flask import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/v1/number2kanji/<name>", methods=["GET", "POST"]) #数字漢数字変換
def number2kanjie(name):
    name = int(name) - int(30)
    return render_template("number2kanji.html", name=name)
    #http://localhost:8888/v1/number2kanji/100


@app.route("/v1/kanji2number/<name>", methods=["GET", "POST"]) #漢数字数字変換
def kanji2number(name):
    name = int(name) + int(30)
    return render_template("kanji2number.html", name=name)
    #http://localhost:8888/v1/kanji2number/100


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)

"""

_______________ FAX 0266-73-9917  電話 0266-73-9853(直通) _____//

2020年10月1日(木) 16:08 Sumiaki Ichikawa <ichikawa@rs.sus.ac.jp>:
>
> 市川です。
> まだ用意していません。
> 受講者はひとりの見通しです。
> リンク作成しますので、待っていてください。
>
> ///￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣ 公立諏訪東京理科大学
> // 〒391-0292 長野県茅野市豊平5000-1   工学部情報応用工学科
> / E-Mail:ichikawa@rs.sus.ac.jp   教授   市川純章
> _______________ FAX 0266-73-9917  電話 0266-73-9853(直通) _____//
>
> 2020年10月1日(木) 10:58 GH20517 <gh20517@ed.sus.ac.jp>:
> >
> > 市川 純章先生
> >
> >
> > ロボット知能特論履修予定の工学マネジメント専攻の吉田秀俊です。
> >
> > SOLAを確認したのですが、ロボット知能特論のページが無かったため連絡させて
> > いただきました。
> > コース名で検索してもSOLA上でヒットしないため確認をお願い致します。
> >
> > 宜しくお願い致します。
"""