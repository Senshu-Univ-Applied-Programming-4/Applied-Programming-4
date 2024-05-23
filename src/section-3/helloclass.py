# File: helloclass.py
# クラス (class)
# https://docs.python.org/ja/3/tutorial/classes.html
# 
class Hello:
	myhello="Hello World"
	def hello(self):
		return self.myhello
	def hello_jp(self):
		localvar="こんにちわ世界"
		return localvar
	def set_hello(self,message):
		self.myhello=message


h=Hello()                     # インスタンスを生成
print(h.myhello)              # myhello変数にアクセス
print(h.hello_jp())           # メソッドhello_jp()を呼び出し
h.set_hello('What\'s up')     # 引数の与え方
print(h.hello())              # プリント
h.myhello="Aloha"             # 直接myhello変数を書き換え
print(h.hello())              # 変化をチェック
h2=Hello()                    # 別のインスタンスh2を生成
print(h2.hello())             # インスタンスh2内の値をプリント
print(h.hello())              # インスタンスh内の値をプリント
Hello.myhello='コニャニャチワ' # クラス変数の値を変える
print(h2.hello())             # インスタンスh2内の値をプリント
print(h.hello())              # インスタンスh内の値をプリント
print(Hello.myhello)          # クラス変数としての値をプリント
h3=Hello()                    # 別のインスタンスh3を生成
print(h3.hello())             # インスタンスh3内の値をプリント
del h                         # インスタンスの消去
del h2                        # インスタンスの消去
del h3                        # インスタンスの消去


