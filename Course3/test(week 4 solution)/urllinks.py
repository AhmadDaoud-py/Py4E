# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('Enter URL: ')
cont = int(input('Enter count: '))
position = int(input('Enter position: '))



print('Retrieving: ' , link)
for i in range(cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    ps = 0
    for tag in tags:
        ps += 1
        if ps == position:
            print('Retrieving: ' , str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break