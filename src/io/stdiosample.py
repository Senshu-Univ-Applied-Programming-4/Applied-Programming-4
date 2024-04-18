# File: stdiosample.py
#
# UNIX Standard I/O 
#
import sys
content=sys.stdin.read()		# 標準入力からすべてを読み込む。
sys.stdout.write(content)		# すべての内容を標準出力に書き出す。

# もしくは次の書き方ができます。
#
# from sys import stdin,stdout,stderr
# content=stdin.read()
# stdout.write(content)
# stderr.write(content)
