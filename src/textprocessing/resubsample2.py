
# File: resubsample2.py
# 正規表現ライブラリ re を使っての正規表現でマッチング
# した文字列を指定の文字に変換する その2
#
# https://docs.python.org/ja/3/library/re.html
#
import re

with open('text01.txt',encoding='utf-8') as f:
	text = f.read()
	pre_text=re.sub("《[あ-ん]*》","",text)
	speaks=re.findall("「.*?」",pre_text) # 最小マッチ
	for t in speaks:
		print(t)

