# File: tcpclie.py
# エコー　クライアント
# https://docs.python.org/ja/3/library/socket.html

import socket

HOST = 'localhost'    # ローカルホストを指定
PORT = 54321          # サーバーのポートを指定
RECVBUFSIZE = 1024

# # ソケットでTCPを開く
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))						# ホストとポートを指定して相手に接続
    s.sendall('こんにちわ世界'.encode('utf-8'))	# データを送る / UTF-8にエンコード
    data = s.recv(RECVBUFSIZE)					# エコーバックを受信
print('Echo:',data.decode('utf-8'))			# UTF-8で出力
