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
    if line.startswith('From'):
        sp = line.split()
        mail.append(sp[1])
    else:
        continue

for word in mail:
    counts[word] = counts.get(word,0)+1
bigcount = None
bigmail = None
for mail, times in counts.items():
    if bigcount is None or times > bigcount:
        bigcount = times
        bigmail = mail
print(bigmail, bigcount)
