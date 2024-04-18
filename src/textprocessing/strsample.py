# File: strsample.py
## pythonにおけるテキスト処理


## 文字列 (テキストシーケンス型)の操作
# https://docs.python.org/ja/3/library/stdtypes.html#text-sequence-type-str

## 初期化
s0='abcdABCD'					# 文字列の初期化
s1=str('abcdABCD')				# strタイプとして明示的に初期化

# 文字列のメソッドの使い方
s0.capitalize()					# 頭のみ大文字
s0.casefold()					# 小文字に変換
s0.count('a')					# 'a'がいくつ含まれるかカウント
s0.count('dA')					# 'dA'がいくつ含まれるかカウント
s0.casefold().count('a')		# すべて小文字に変換した後に'a'をカウント
# 日本語のeocode/decode
s2='日本語文字列'
bs2=s2.encode(encoding='utf-8')	# 日本語文字列(utf-8)をバイト列に変換
s3=bs2.decode(encoding='utf-8')	# バイト列を日本語文字列 (utf-8)に変換
print(s2 == s3)					# 中身が同じか
print(id(s2) == id(s3))			# オブジェクトが同じか
# 文字列中の文字をみつける
s4='abcdABCDabcdABCD'
s4.find('AB')					# 文字'AB'が現れた先頭の場所
s4.index('AB')					# 文字'AB'が現れた先頭の場所
s4.rfind('AB')					# 文字'AB'が現れた最後の場所(逆から探す)
s4.rindex('AB')					# 文字'AB'が現れた最後の場所(逆から探す)
# 文字の置き換え
s4='abcdABCDabcdABCD'
s4x=s4.replace('a','x')			# aをxに置換する
s4xyz=s4.replace('abc','xyz')	# abcをxyzに置換する
# 文字のフォーマット
s5="1と2を足すと{0}になります。".format(1+2)
print(s5)
a=10
b=20
s5x="{0}と{1}を足すと{2}になります。".format(a,b,a+b)
print(s5x)
s5y="{0}を{1}で割ると{2:.1f}になります。".format(a,b,a/b)
print(s5y)
# 文字の並びの分割
s6a='Item0 Item1 Item2'			# ワードとワードの間が空白で区切られている
s6a1=s6a.split()				# リストになったデータが返却される
s6b='項目0,項目1,項目2'			# ワードとワードがカンマ(,)で区切られている
s6b1=s6b.split(',')				# 区切りにカンマ(,)を指定する
# 文字の除去
s7='文字列\n'				  # 行末に改行コード\nがついている
print(s7.strip())			  # 行末の改行コードをストリップ(取り去る)
s7x=' ,文字列, '			  # 前もしくは後ろの余計な文字を処理する
print(s7x.strip(', '))		  # カンマと空白をストリップ（取り去る)
