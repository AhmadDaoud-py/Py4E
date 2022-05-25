fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('Sorry unable to open the file try again')
    quit()

fh = open(fname)
count = 0
lst = list()
for line in fh:
    if line.startswith('From'):
        sp = line.split()
        if len(sp)<1:
            continue
        if sp[1] in lst:
            continue
        lst.append(sp[1])
        count = 1 + count
for mail in lst:
    print(mail)
print("There were", count, "lines in the file with From as the first word")

#working same as autograder
# fhand = open("mbox-short.txt")
# count = 0
# for line in fhand:
#     line = line.rstrip()
#     if line == "": continue
#
#     words = line.split()
#     if words[0] !="From": continue
#
#     print(words[1])
#     count = count+1
#
# print ("There were", count, "lines in the file with From as the first word")
