
##  File: utf8sample.py

# 文字列をバイナリーにする
# バイナリーを文字列にする
#
# 文字列はUTF-8がデフォルトであることが前提

orig_s='こんにちわ世界'

# バイナリーに変換する
x=orig_s.encode('utf-8')
print(x)

# バイナリーをUTF-8の文字列にする
s=x.decode('utf-8')
print(s)
