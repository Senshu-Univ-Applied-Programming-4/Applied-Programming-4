#
# File: threadsample.py
#
import sys
import os
import time
import threading

def threading_module(msg):
	time.sleep(2)
	print("Thread Start: ",msg,"pid(",os.getpid(),")")
	for t in range(5):
		time.sleep(1)			# 1秒の待ち
		print(msg+':'+str(t))	# 何のプロセスが何回目かを出力

	print("Thread Finish: ",msg,"pid(",os.getpid(),")")

	

if __name__ == "__main__":
	thread_queue=[]				# スレッドを保持しておくため
	for msg in [ 'A','B','C','D','E']:
		th = threading.Thread(target=threading_module, args=(msg,))
		th.start()
		thread_queue.append(th)

	print("***Waiting Join Thread***")
	
	for th in thread_queue:		# スレッド終了時の後処理
		th.join()				# スレッド終了までブロッキングされる
		print(th)
