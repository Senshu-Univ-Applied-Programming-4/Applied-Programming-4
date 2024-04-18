# File: whilesample.py
# while文による単純な繰り返し

# 単純ループ
i=0
while i < 10:
	i += 1
	print(i)

# continue文

i=0
while i < 10:
	i += 1
	if i < 3:
		continue
	print(i)
# break文

i=0
while i < 10:
	i += 1
	if i > 7:
		break
	print(i)
# else文

i=0
while i < 10:
	i += 1
	print(i)
else:
	print("finish loop")
