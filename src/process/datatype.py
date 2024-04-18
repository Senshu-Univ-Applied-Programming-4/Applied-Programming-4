# File: datatype.py
# 子プロセスを生成する
#
import sys
import os
import time
from multiprocessing import Process

#子プロセス 
def child_process(msg):
	time.sleep(3)				# 3秒まってから処理開始
	print(msg,os.getpid())		# 子プロセスのpid
	for t in range(5):
		time.sleep(1)			# 1秒の待ち
		print(msg+':'+str(t))	# 何のプロセスが何回目かを出力
	sys.exit(0)					# 子プロセス終了

if __name__ == '__main__':
	process_queue=[]				# 子プロセスを保持しておくため
	for msg in [ 'A','B','C','D','E']:
		p = Process(target=child_process, args=(msg,)) # プロセスを生成
		p.start()									   # プロセススタート
		process_queue.append(p)		# キューにつめる
		
	print("***Waiting Join Child Process***")

	for p in process_queue:		# 子プロセスの終了時の後処理
		p.join()				# 子プロセス終了までブロッキングされる
		print(p)
