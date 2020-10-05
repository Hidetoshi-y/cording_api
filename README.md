# 目的
コーディングテスト

WebAPIのサービス作成

# 内容物（ローカルで関係のあるもの）
- .gitignore 
- README.md 
- app.py
- run.sh
- setup.sh
- test_check
- requirements.txt

# 動作環境
Python 3.6.9

ライブラリ -> requirements.txt参照


## templates

templates/

    |-mainpage.html

    |-number2kanji.html

    |-kanji2number.html

    |-erroe.html

# 動かし方
---初回-----

0. `./setup.sh`

---実行---

1. `./run.sh`

2. ローカルで動作確認する場合

`0.0.0.0:5002/v1/kanji2number/{}`

`0.0.0.0:5002/v1/kanji2number/{}`

3. WebAPIでアクセスする場合

`https://yamada.jo.sus.ac.jp/v1/kanji2number/{}`

`https://yamada.jo.sus.ac.jp/v1/number2kanji/{}`

# 参考サイト

FlaskのAPIの例

https://qiita.com/tomson784/items/406281bef7a5b2eb3cd8

FlaskのAPIの例２

https://sitest.jp/blog/?p=10459ß

render_templateの利用

https://qiita.com/nagataaaas/items/4662237cfb7b92f0f839

配列の削除を配列で

https://qiita.com/saa/items/d18a36d764c74fc8bf26

