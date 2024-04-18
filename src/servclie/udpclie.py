# File: udpclie.py
# エコー　クライアント
# https://docs.python.org/ja/3/library/socket.html

import socket

HOST = 'localhost'    # ローカルホストを指定
PORT = 12345          # サーバーのポートを指定
RECVBUFSIZE = 1024

#  UDPのソケットを開く
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	send_len = s.sendto('こんにちわ世界'.encode('utf-8'), (HOST,PORT)) # 送出
	data, addr = s.recvfrom(RECVBUFSIZE)	# 返りメッセージを受信
	print('Echo:',data.decode('utf-8'))			# UTF-8で出力

