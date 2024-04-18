# File: setsamole.py
#

animal={'dog','cat','fish','lizard'}
mammal={'dog','cat'}
pet={'dog','dog','lizard'}

##
## 重複はなくなる
##
print(animal)
print(mammal)
print(pet)
# 飼っていない動物は?
print(animal - pet)

# ペットで哺乳類以外
print(pet - mammal)
# ペットに犬はいる?
print( 'dog' in pet)

# リンゴは動物?
print( 'apple' in animal)

# トカゲは飼っていない
print( 'lizard' not in pet)

# lizardの文字列の中に'rd'はあるか
print( 'rd' in 'lizard')
for i in animal:
	print('loop',i)
