# Con.py
n = input("Pick a number 1-12: ")
a = 'Demon'
b = 'Naruto'
c = 'Bleach'
d = 'DBZ'
e = 'Darwins game'

n = float(n)

if n in range(10,12):
    print(e)
elif n in range(8,9):
    print(d)
elif n in range(6,7):
    print(c)
elif n in range(4,5):
    print(b)
elif n in range(1,3):
    print(a)
else:
    print('Please select a number between 1-10')
    quit()
