# File: tuplesample.py
# タプル (組み合わせ)
t=1,"aaa",2,["ccc","ddd"]
print(t)
# tupleはimmutableなのでエラーになる
#t[0]=2
# Sequence Unpacking
i,s,j,l=t
print(i,s,j,l)

# タプルでイテレーションをする
for i in t:
	print('loop',i)
