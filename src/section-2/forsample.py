# File: forsample.py
# 辞書の要素はタプルとなる

prfm_dict={ 'a-chan': 'Perfume', 'KASHIYUKA': 'Perfume', 'NOCCHi': 'Perfume'}

for t in prfm_dict.items():
	print(t)
# passは何もしない
# elseはforが終了時に実行される.

for m,p in prfm_dict.items():
	if p == 'Perfume':
		pass
	else:
		print('Dictionary is compromised',m,p)
		break
else:
	print('Dictionary check is finished')
# 回数ループに必須のrange() : ゼロオリジン

# iterableなオブジェクトを返す関数
print(range(10))
for i in range(5):
	print(i)

# 範囲も使える
for i in range(20,23):
	print(i)

# ステップも刻める
for i in range(0,100,20):
	print(i)

# こんな使い方も出来る
print(sum(range(10)))
