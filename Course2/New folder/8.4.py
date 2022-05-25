
fname = input("Enter file name: ")

try:
    fh = open(fname)
except Exception as e:
    print("Sorry unable to open the file",fh)
    quit()

lst = list()
for line in fh:
    spl = line.rstrip().split()
    #print(spl)
    for word in spl:
        if word in lst:
            continue
        lst.append(word)
        #print(lst)


lst.sort()

print(lst)
