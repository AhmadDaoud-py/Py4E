score = input("Enter Score: ")
try:
    inp=float(score)
except:
    print('The input must be a valid number')
    quit()
x=int(inp)
if x >1 or x <0:
    print('The range must be between 0.0 and 1.0')
elif inp >= 0.9:
    print('A')
elif inp >= 0.8:
    print('B')
elif inp >= 0.7:
    print('C')
elif inp >=0.6:
    print('D')
elif inp <0.6 & inp >0:
    print('F')
