# File: skipruby.py
start_ruby='《'					# ルビの開始
end_ruby='》'					# ルビの終了


with open("text01.txt",encoding='utf-8') as f:
	for l in f:					# ファイルから1行取り出す
		flag=False				# フラグをオフにする
		for c in l:				# 行から1文字取り出す
			if c == start_ruby:	# ルビの開始の文字と一致するか
				flag=True		# フラグをオンにする
				continue		# その文字を飛ばして次の文字に進む
			if c == end_ruby:	# ルビの終了の文字と一致するか
				flag=False		# フラグをオフにする
				continue		# その文字を飛ばして次の文字に進む
			if (flag != True ):	# フラグがオンではない場合、1文字出力する
				print(c,end='')
