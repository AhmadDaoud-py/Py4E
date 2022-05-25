name = input("Enter file:")
if len(name) < 1:
    name = "words.txt"
try:
    handle = open(name)
except:
    print("Error opening file")

dicwords =dict()

for line in handle:
    line = line.strip()
    words = line.split()
    for word in words:
        dicwords[word] = dicwords.get(word,0)+1


for k , v in dicwords.items():
    print(k,v)
