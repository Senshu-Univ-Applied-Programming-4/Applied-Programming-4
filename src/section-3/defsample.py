# File: defsample.py
# 関数 (function)

## 
def funcsample(x,y):
	return x+y
	
print(funcsample(10,20))
print(funcsample("abc","efg"))

f=funcsample

print(f(10,20))
print(f("abc","efg"))


def funca(x,y):
	return(x,y)

def funcb(x,y):
	return(y,x)

funcs=[funca,funcb]

print(funcs[0](1,2))
print(funcs[1](1,2))

def triadd(k=10,l=20,m=30):
    return (k+l+m)

print(triadd())
print(triadd(30))
print(triadd(30,50))
print(triadd(30,50,60))
