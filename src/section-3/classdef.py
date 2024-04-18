# File: classdef.py
# クラス (class)

class NumberPool():
	def __init__(self):
		self.pool_of_numbers=[] # list型のインスタンス変数を作成

	def add(self,number):
		if (type(number) == int ): #　渡されたオブジェクトが整数ならば
			self.pool_of_numbers.append(number)
			return self.pool_of_numbers
		else:
			return None			# 整数ではなかった
	
	def get(self):
		return self.pool_of_numbers # すべてを返す

	def del_odd(self):			# 奇数のみ消す
		even=[]
		for i in self.pool_of_numbers:
			if (i % 2) == 0:
				even.append(i)
		self.pool_of_numbers=even
		return self.pool_of_numbers

	def join(self,pool_num):		# poolを連結する
		if (type(pool_num) == NumberPool):
			self.pool_of_numbers += pool_num.get()
			return self.pool_of_numbers
		else:
			return None

p0 = NumberPool()
p0.add(100)
p0.add(99)
print(p0.get())
print(p0.pool_of_numbers)

p1 = NumberPool()
p1.add(87)
p1.add(22)
print(p1.get())
print(p1.pool_of_numbers)

p0.del_odd()
print(p0.get())

p1.join(p0)

print(p1.get())
print(p0.get())

