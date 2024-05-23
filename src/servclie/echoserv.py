#
# File: echoserv.py
# オリジナルは
# https://docs.python.org/ja/3/library/socketserver.html
#

import socketserver
import sys
import os 
import signal

##
## 実装されるハンドラ
##
class LocalTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
    # 接続されるハンドラ
        print(self.client_address[0]) # 接続元IPアドレス
        print(os.getpid())            # 自分のPID
        while True:
            try:
                self.data = self.request.recv(1024)
                print(self.data.decode('UTF-8'),end='')
                self.request.sendall(self.data)
            except:
                return 

    def finish(self):
        print("**Finish**")
        print(os.getpid())
        return socketserver.BaseRequestHandler.finish(self)

def finish_all(signal,frame):   # プログラムを終了
    sys.exit(0)

# Control-C シグナルを拾った時の処理
signal.signal(signal.SIGINT, finish_all)

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0" , 54321
    #
    # TCPサーバーを作る / フォークする
    #
    with socketserver.ForkingTCPServer((HOST, PORT), LocalTCPHandler) as server:
        server.serve_forever()

