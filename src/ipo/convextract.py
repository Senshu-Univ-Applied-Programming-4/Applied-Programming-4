# File: convextract.py
# 文章から発話部分を抜き出す。

lines=[]						# 発話テキストを保持するリスト
with open('text02.txt',encoding='utf-8') as f:	# テキスト読み込み用としてオープン
	for l in f:
		if '「' in l :			# 行の中に'「'がある (発話がある)
			speak=''			# 発話を保持するための文字列
			for e in l:			# 行を文字単位でチェックしていく
				if e == '「':
					speak = speak+e # 文字を加える
					continue		# 次に進む
				if e == '」':		# 発話が終了
					speak = speak+e
					lines.append(speak) # リストに追加
					speak=''			# 次のために初期化
				if speak != '':			# 発話の最中なら文字列に文字を加える
					speak=speak + e

with open('conv.txt','w',encoding='utf-8') as f:	# 書き出しファイルをオープン
	for l in lines:				# リストの要素(発話)を1つ取り出す
		if '《' in l:			# 文字列の中に読みがながあるか
			flag=False			# あればフラグをオフにする
			for e in l:			# 一文字づつチェックする
				if e == '《':	# 読みがな開始
					flag=True	# フラグをオン
					continue	# スキップ
				if e == '》':	# 読みがな終了
					flag=False	# フラグをオフ
					continue	# スキップ
				if flag == False: # フラグが立っていない（読みがなではない）
					f.write(e)	  # ファイルに書き出し
			else:
				f.write('\n')	# 一行終わると改行を加える
		else:
			f.write(l+'\n')		# 文字列の中に読みがながなかったので書き出す
