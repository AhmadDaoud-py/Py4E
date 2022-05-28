import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Enter location: ")
jsonh = urllib.request.urlopen(address).read().decode()

print("Retriving",address)
print("Retrived", len(jsonh),"charachters")

parsedJson = json.loads(jsonh)


count = list()



for user in parsedJson['comments']:

    count.append(int(user['count']))

print("Count:", len(count))
print("Sum:",sum(count))
