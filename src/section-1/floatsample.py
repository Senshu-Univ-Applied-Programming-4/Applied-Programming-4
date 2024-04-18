# File: floatsample.py
x=1.0
y=2.0
z=3.0
print(x/y)
print((x/y)*z)

## 浮動小数点の精度 IEEE-754 double precision
print(x/z)
## 値は 0.30000000000000004 になる
print(0.1+0.2)
# 多倍長浮動小数点
# pip install bigfloat
# GNU MPFR is required
# https://www.mpfr.org/
# https://pypi.org/project/bigfloat/
#

#from bigfloat import *
#print (sqrt(9+4))
#with precision(8092):
#    print (sqrt(9+4))
