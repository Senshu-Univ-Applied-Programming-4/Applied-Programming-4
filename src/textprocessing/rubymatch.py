# File: rubymatch.py
# 青空文庫のテキスト中にあるルビを抜き出す
#
import re
with open("text01.txt",encoding="utf-8") as f:
	text = f.read()
	match_ruby=re.findall("《[あ-ん]*》",text)
	##print(match_ruby)
	print("ルビの数: ",len(match_ruby))
