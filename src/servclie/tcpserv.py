# File: tcpserv.py
#
# エコーサーバー 
# https://docs.python.org/ja/3/library/socket.html
# 
import socket

HOST = '0.0.0.0'				# すべてのIPアドレスからの接続を許す
PORT = 54321					# ポート番号 / ダイナミック・ポートの領域を利用
RECVBUFSIZE = 1024

# TCPソケットを開く
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))	# ソケットをポートにバインド
	s.listen(1)					# 接続準備
	while True:
		conn, addr = s.accept()		# 接続待ち
		with conn:
			print('Connected by', addr)
			while True:
				data = conn.recv(RECVBUFSIZE) # 受信
				if not data:				  # データがなければ
					break					  # 接続終了
				conn.sendall(data)			  # 受信したデータをエコーバック
