n = input('Select a number 1-10: ')

n = float(n)

if n in range(1,11,2):
    print('Odd number')
if n in range(1,11,1):
        print('Even number')
