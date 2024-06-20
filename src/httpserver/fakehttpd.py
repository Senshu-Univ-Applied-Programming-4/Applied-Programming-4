import sys
import os
import signal

from http.server import BaseHTTPRequestHandler
import socketserver

import xml.etree.ElementTree as ET
import xml.dom.minidom as Dom


PORT = 8080


class LocalHandler(BaseHTTPRequestHandler):
		
	def log_message(self, format, *args):
		# https://github.com/python/cpython/blob/v3.6.8/Lib/http/server.py#L552-L572
		##sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(),self.log_date_time_string(),format%args))
		#
		# XML format output
		#
		logentry=ET.Element('access',{'version':'1.0' ,'encoding':'utf-8'})
		date=ET.SubElement(logentry,'date')
		date.text=self.log_date_time_string()
		path=ET.SubElement(logentry,'path')
		path.text=self.path
		address=ET.SubElement(logentry,'address')
		address.text=self.address_string()
		request=ET.SubElement(logentry,'request')
		request.text=format%args
		header=ET.SubElement(logentry,'header')
		header.text=str(self.headers)
		
		## 文字列に変換
		xml_string = ET.tostring(logentry)
		## キレイに整形
		pretty_xml = Dom.parseString(xml_string) 
		print(pretty_xml.toprettyxml())


	def do_HEAD(self):
		self.do_response()

	def do_GET(self):
		self.do_response()
		
	def do_POST(self):
		self.do_response()

	def do_response(self):
		self.server_version="httpd"
		self.sys_version="Embedded System (fake)"
		self.send_response(200)
		self.send_header('Content-Type', 'text/html; charset=utf-8')
		self.end_headers()
		self.wfile.write(b'\n\n<!DOCTYPE html>\n<html>\n<head>\n<title>Access Failed</title>\n<meta http-equiv="cache-control" content="no-cache">\n</head>\n<body>\nAccess Failed\n</body>\n</html>\n')
		


#
# Signal 
#
def signal_finish(signal,frame):
	print('Get signal {}'.format(signal))
	os._exit(0)
##	sys.exit(0)

signal.signal(signal.SIGINT, signal_finish)
signal.signal(signal.SIGTERM, signal_finish)


print('*** START Simple HTTPD ***')

## Reusesable Address
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), LocalHandler) as httpd:
	httpd.serve_forever()
