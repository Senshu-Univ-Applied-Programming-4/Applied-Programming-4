# File: resample.py
#
# 正規表現ライブラリ re を使ってのマッチング
#
# https://docs.python.org/ja/3/library/re.html
#
import re

# 文字列を用意する
textSet = ["abc","feg","hij","cba","gef","jih","afh","bei","cgj"]

# マッチさせる正規表現のパターン
regexp_pattern="^ab"
for text in textSet:
	result=re.search(regexp_pattern,text) # 文字列の中からパターンを探す
	if result != None :					  # マッチしたら
		print(regexp_pattern,text,result.group(),result.span())

