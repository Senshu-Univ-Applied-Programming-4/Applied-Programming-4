# File: dictsample.py
# dict (辞書)

# 1対1のマッピング
prfm={ 'a-chan': 'Perfume', 'KASHIYUKA': 'Perfume', 'NOCCHi': 'Perfume'}
print(prfm)
# 誤った例
error_prfm={ 'Perfume':'A-CHAN', 'Perfume':'B-KASHIYUKA',  'Perfume':'C-NOCCHi'}
print(error_prfm)
# キー(Key)で値(Value)アクセス
print(prfm['a-chan'])
print(prfm['KASHIYUKA'])
print(prfm['NOCCHi'])
# 辞書の追加
#
team_prfm_dict={ 'MIKIKO': 'Team Perfume'}
prfm.update(team_prfm_dict)
print(prfm)
# タプルを値(Value)にした辞書

prfm_wt_dict={
	2012: ('Perfume WORLD TOUR 1st','B00MXXEXUA'),
	2013: ('Perfume WORLD TOUR 2nd','B00MXXEXUU'),
	2014: ('Perfume WORLD TOUR 3rd','B00YRSC39W'),
	2019: ('Perfume WORLD TOUR 4th ｢FUTURE POP｣','B07TGCNDS3')}
# KeyとValueの参照の方法
for key,value in prfm_wt_dict.items():
	print(key,"->",value)
# キーがソートされてlistで返される
print(sorted(prfm_wt_dict))
published_years=sorted(prfm_wt_dict)
# 最後の(最新)のエントリー
# 最新のPerfumeが最高のPerfume
print(published_years[-1])
print(prfm_wt_dict[published_years[-1]])
#動かさなくても何をしたいか大体見当がつくはず
live_title,amazon_dp=prfm_wt_dict[published_years[-1]]
print(live_title)
print("https://amazon.co.jp/dp/"+amazon_dp)
