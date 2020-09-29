from flask import Flask, request, jsonify
from flask import request, render_template



app = Flask(__name__)

@app.route('/')#ルートにアクセスした際の処理
def index():
   return 'Hello flask'

@app.route('/user')#userにアクセスした際の処理
def user():
   user_id = request.args.get('id')#指定された文字なrば
   return search_user(user_id)#search_user関数の引数に取得した値を入れて実行する。

def search_user(user_id):
   # 例えばここに、DBからユーザを取得する処理を書くなどできます
   # 今回はひとまずユーザデータのJSONを固定値で書いてみます

   user = {
    'id': user_id,#引数を表示するだけ
    'name': 'Tarou',
    'age': 23
   }

   return jsonify(user)#json形式で引数を表示する？

if __name__ == '__main__':
    app.run()