#
# XML Generator
#
import xml.etree.ElementTree as ET
import xml.dom.minidom as Dom
import datetime

## XMLのトップのエレメントを作る
logentry=ET.Element('logging',{'version':'1.0' ,'encoding':'utf-8'})

for e in range(20):
	## entryのトップ
	entry=ET.SubElement(logentry,'entry')
	## entryの中の要素 number
	number=ET.SubElement(entry,'number')
	number.text=str(e)
	## entryの中の要素 date
	date=ET.SubElement(entry,'date')
	date.text=str(datetime.datetime.today())


## 文字列に変換
xml_string = ET.tostring(logentry)
## キレイに整形
pretty_xml = Dom.parseString(xml_string) 

print(pretty_xml.toprettyxml())



