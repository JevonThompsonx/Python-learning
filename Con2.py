# Con.py
n = input("Pick a number 1-12: ")
a = 'Demon'
b = 'Naruto'
c = 'Bleach'
d = 'DBZ'
e = 'Darwins game'

n = int(n)

def anime(list):
    if anime == 'Demon slayer':
        print('1-2')
    if anime == 'Naruto':
        print('3-4')
    if anime == 'Bleach':
        print('5-7')
    if anime == 'DBZ':
        print('Darwins game')

if n in range(10,12):
    print(e)
    anime(Darwins game)
elif n in range(8,9):
    print(d)
    anime(DBZ)
elif n in range(6,7):
    print(c)
    anime(Bleach)
elif n in range(4,5):
    print(b)
    anime(Naruto)
elif n in range(1,3):
    print(a)
    anime(Demon Slayer)
else:
    print('Please select a number between 1-10')
    quit()
