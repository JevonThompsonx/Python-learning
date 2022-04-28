hrs = input("Enter Hours:")
r = input("Pay rate: ")

hrs = float(hrs)
r = float(r)
def computepay(hrs,r):
    x = hrs
    y = r
    y2 = r * 1.5
    overtime = (x - 40) * y2
    reg = (40 * y)
    if hrs > 40:
        return overtime + reg
    else:
        return x * y


p = computepay(hrs,r)
print("Pay", p)
