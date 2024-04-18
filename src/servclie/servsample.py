
# File: servsample.py
#
# エコーサーバー 
# https://docs.python.org/ja/3/library/socket.html
#

import socket
HOST = '0.0.0.0'# すべてのIPアドレスからの接続を許す
PORT = 54321					# ポート番号 / ダイナミック・ポートの領域を利用
# with構文を使って処理を閉じる書き方
# ソケットでTCP/IPを開く
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))	# ソケットをポートにバインド
	s.listen(1)					# 接続開始
	conn, addr = s.accept()		# 接続待ち
	with conn:
		print('Connected by', addr)
		while True:				# 無限ループ
			data = conn.recv(1024)
			if not data: break
			conn.sendall(data)
