name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Error opening file")


mail = list()
counts = dict()

for line in handle:
    if line.startswith('From '):
        sp = line.split()
        x=sp[5][ : sp[5].find(':')]
        mail.append(x)
    else:
        continue

for word in mail:
    counts[word] = counts.get(word,0)+1

lst = list()

for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

for val, key in lst[:10]:
    print(key, val)