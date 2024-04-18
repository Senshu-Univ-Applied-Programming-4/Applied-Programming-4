# File: udpserv.py
# エコーサーバー 
# https://docs.python.org/ja/3/library/socket.html
# 
import socket

HOST = '0.0.0.0'				# すべてのIPアドレスからの接続を許す
PORT = 12345					# ポート番号 / ダイナミック・ポートの領域を利用
RECVBUFSIZE = 1024

# UDPのソケットを開く
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
	s.bind((HOST, PORT))	# ソケットをポートにバインド
	while True:				# 無限ループ
		data, addr = s.recvfrom(RECVBUFSIZE) # 受信
		print(data.decode('utf-8'),addr)	 # 出力
		s.sendto(data,addr)					 # エコーバック
