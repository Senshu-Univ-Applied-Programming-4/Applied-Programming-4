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
		content_length = int(self.headers['content-length'])
		print("Post content length:",content_length)
		print("----")
		print(self.rfile.read(content_length).decode('utf-8'))
		print("----")

		self.send_response(200)
		self.send_header('Content-Type', 'text/plain; charset=utf-8')
		self.end_headers()
		self.wfile.write(b'Done.')

		
	def do_response(self):
		self.send_response(404)
		self.send_header('Content-Type', 'text/plain; charset=utf-8')
		self.end_headers()
		self.wfile.write(b'Response')

		
	


print('*** START Simple HTTPD ***')
## Reusesable Address
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), LocalHandler) as httpd:
	httpd.serve_forever()
