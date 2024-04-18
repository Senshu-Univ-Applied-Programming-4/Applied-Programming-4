## File: withopensample.py

# ファイル（自分自身）をwith文内でオープンし、読み込み
# 出力する (クローズは自動)

with open("withopensample.py",encoding='utf-8') as f:
	print(f.read(),end='')
