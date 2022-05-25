# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Sorry unable to open the file:",fname,"please try again later")

count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count +1
    pos = line.find(':')
    no = float ( line[pos+1 :].strip())
    tot = tot + no


print("Average spam confidence:",tot / count)
