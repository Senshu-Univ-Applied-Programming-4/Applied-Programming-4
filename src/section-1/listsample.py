# File: listsample.py
#リスト

a=[1,2,3,4,5]
print(a)
print(a[2])
# リストはmutable
# cf. str type
a[2]=10
print(a)

# 区間を入れ替える
a[3:5]=[11,12]
print(a)
# リストの要素を取り出し
#
for i in a:
	print("loop",i)
#
# リストのリスト
#
b = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]
print(b)
#
# ネストループ
for i in b:
	for j in i:
		print("loop",j)
#
# オブジェクトをリスト要素として持つ
#
#
c=[1,'abc',2,'efg',[4,5,6]]
print(c)
# リストのメソッド
a.append(999)
print(a)
# mutableなデータタイプに対して
# 消去を行うdel文
del a[0]
print(a)
print(len(a))
