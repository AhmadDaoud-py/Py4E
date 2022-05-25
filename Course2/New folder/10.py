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


lst = list()

for key, val in dicwords.items():
    newtuples = (val, key)
    lst.append(newtuples)
print('****first*****')
print(lst)

lst = sorted(lst, reverse=True)
print('****second*****')
print(lst)

print('****top 10*****')

for val, key in lst[:10]:
    print(key, val)