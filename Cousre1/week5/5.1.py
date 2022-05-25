num = 0
tot = 0.0

while True:
    sval = input('Enter a number : ')
    if sval == 'Done' or sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print ('invalid number')
        continue
    num = num + 1
    tot = tot + fval

print(tot,num, tot/num)
