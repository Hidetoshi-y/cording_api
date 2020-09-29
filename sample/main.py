from flask import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])#ルートで表示するページ
def main_page():
    return render_template("mainpage.html")


@app.route("/var/too/<name>", methods=["GET", "POST"])#動作するページ
def namepage(name):
    return render_template("name.html", name=name)

"""最初の状態
@app.route("/<name>", methods=["GET", "POST"])#動作するページ
def namepage(name):
    return render_template("name.html", name=name)
"""


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)