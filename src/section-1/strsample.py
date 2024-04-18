# File: strsample.py

#文字列(連続した文字並び) Built-in type str
print('abc')

# 連結
print('abc' 'def')
s='abcdef'
print(s)
# immutable and error statement
# s[0]='X'

# 新しいstrオブジェクトを作り連結
s='abcdef'
s=s+'ghij'
print(s)
#組み込み関数len() / メソッドはない
print(len(s))
# 文字列内の文字にアクセス
print(s[0])
print(s[-1])
print(s[2:])
print(s[:2])
print(s[2:5])
print(s[5:2])
t=2
k=5
print(s[k:t]) # エラーとはならず空文字列を返す
# メソッド
# Space Splited String
sss='abc def ghi'
print(sss.split())

# Comma Separated Value
str_csv='abc,def,ghi'
print(str_csv.split())
print(str_csv.split(','))
#文字列
a=str('abc')
print(a,type(a))

#バイト列 (Byte-like Object)
ab=b'abc'
print(ab,type(ab))

## Asciiコードの値が出力
print(ab[0])

if ab[0] == a[0]:
	print("OK")
else:
	print("NG")

