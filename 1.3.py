hrs = input("Enter Hours: ")
h = float(hrs)

rate = input('Rate: ')
r = float(rate)

if h > 40:
    x = (h - 40) * (r * 1.5) + (h * r)
else:
    x = r * h
print(x)    
