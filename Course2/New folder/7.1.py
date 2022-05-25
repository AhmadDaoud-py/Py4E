# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
content = fh.read()
upper = content.upper().rstrip()
print(upper)
