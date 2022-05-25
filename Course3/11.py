import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_1554331.txt"
try:
    handle = open(name)
except:
    print("Error opening file")
lst = list()
for line in handle:
    line = line.rstrip()
    num = re.findall('[0-9]+', line)
    if len(num) == 0: continue
    for each in num:
        eachnum = int(each)
        lst.append(eachnum)

print(sum(lst))

