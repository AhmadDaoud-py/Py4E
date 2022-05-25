def computepay(h, r):
    if h <= 40:
        pay= h* (r * 1.5)
        return pay
    elif h > 40:
        pay = 40 * r + (h-40)*r*1.5
        return pay
    else:
        print('somthing went wrong...')

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error: you have to enter numeric value')
    quit()
p = computepay(h, r)
print("Pay", p)
