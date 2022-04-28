# Con.py
n = input("Pick a number 1-10: ")
a = 'Demon slayer'
b = 'Naruto'
c = 'Bleach'
d = 'DBZ'
e = 'Darwins game'

n = int(n)

if n in range(0,3):
    print(a)
elif n in range(3,6):
    print(b)
elif n in range(6,8):
    print(c)
elif n in range(8,11):
    print(e)
else:
    print('Please select a number between 1-10')
    quit()
