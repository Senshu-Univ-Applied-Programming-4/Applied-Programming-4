# File: ifsample.py
# if 内容が同じか、オブジェクトが同じか

a= 'abc'
b= 'a' 'b' 'c'

print(a)
print(b)

if a == b:
	print('a==b')
else:
	print('a!=b')

if a is b:
	print('a is b')
else:
	print('a is not b')

print(id(a))
print(id(b))
# if 内容が同じか？オブジェクトが同じか？

a= 'abc'
b= 'a' 'b'
b= b + 'c'

print(a)
print(b)

if a == b:
	print('a==b')
else:
	print('a!=b')

if a is b:
	print('a is b')
else:
	print('a is not b')

print(id(a))
print(id(b))
	
#aとbは同じオブジェクト
a='abc'
b='abc'
if ( id(a) == id(b) ):
	print("a is b")
else:
	print("a is not b")
	
b='ab'
b=b+'c'

#aとbは異なるオブジェクト
if ( id(a) == id(b) ):
	print("a is b")
else:
	print("a is not b")

#cとbは同じオブジェクト
c=b
print(id(b))
print(id(c))
a='abc'
b='efg'
c='abc'
if ( a == b ):
	print('a==b')
elif ( a == c ):
	print('a==c')
else:
	print('a != b and a != c')

