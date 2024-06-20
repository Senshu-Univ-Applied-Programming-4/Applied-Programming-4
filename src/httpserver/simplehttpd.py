#
# Refernce
# https://docs.python.org/ja/3/library/http.server.html
# 
from http.server import BaseHTTPRequestHandler
import socketserver

PORT = 8080

class LocalHandler(BaseHTTPRequestHandler):

	def do_HEAD(self):
		self.do_response()
	def do_GET(self):
		self.do_response()
	def do_POST(self):
		self.do_response()
		
	def do_response(self):
		print('PATH: {}'.format(self.path))
		address,port=self.client_address
		print('ADDRESS: {}'.format(address))
		print('PORT: {}'.format(port))
		print('{}'.format(self.headers))
		self.send_response(404)
		self.send_header('Content-Type', 'text/plain; charset=utf-8')
		self.end_headers()



print('*** START Simple HTTPD ***')
## Reusesable Address
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), LocalHandler) as httpd:
	httpd.serve_forever()
