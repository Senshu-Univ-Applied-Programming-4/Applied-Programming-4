
# File: resubsample.py
# 正規表現ライブラリ re を使っての正規表現でマッチング
# した文字列を指定の文字に変換する
#
# https://docs.python.org/ja/3/library/re.html
#
import re

with open('text01.txt',encoding='utf-8') as f:
	text = f.read()
	print(re.sub("《[あ-ん]*》","【削除】",text))

