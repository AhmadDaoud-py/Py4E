import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter location: ")
xml = urllib.request.urlopen(address).read().decode()


print("Retriving",address)
print("Retrived", len(xml),"charachters")

tree = ET.fromstring(xml)

tags = tree.findall('comments/comment')
count = list()
for tag in tags:
    count.append(int(tag.find('count').text))


print('count:',len(count))
print('Sum:',sum(count))
