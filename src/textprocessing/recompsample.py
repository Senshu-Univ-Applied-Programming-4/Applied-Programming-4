
# File: recompsample.py
# 正規表現ライブラリ re を使ってのマッチング
# 事前にcompileさせる方式
#
# https://docs.python.org/ja/3/library/re.html
#
import re

# 文字列を用意する
textSet = ["abc","feg","hij","cba","gef","jih","afh","bei","cgj"]

# マッチさせる正規表現のパターン
regexp_comp=re.compile("[a-zA-Z0-9]+j")
for text in textSet:
	result=regexp_comp.match(text) # 文字列の中からパターンを探す
	if result != None :					  # マッチしたら
		print(text)
