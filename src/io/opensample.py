## File: opensample.py

# ファイル（自分自身）をオープンし、読み込み
# 出力した後、クローズする

f = open("opensample.py",encoding='utf-8')
print(f.read(),end='')
f.close()

