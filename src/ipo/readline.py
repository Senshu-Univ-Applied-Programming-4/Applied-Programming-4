# File: readline.py
#
# ファイル（自分自身）をwith文内でオープンし、1行つづ読み込み
# 先頭に行番号を加えて出力する (クローズは自動)

with open("text01.txt", encoding='utf-8') as f:
	linecounter=1
	for l in f:
		print(linecounter,l,end='')
		linecounter+=1
		
# openで明示的に文字コードを指定する場合はencodingの引数をつかいます。
# (Windows上では必要です)

