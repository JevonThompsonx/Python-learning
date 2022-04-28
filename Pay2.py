x = input('How many hours? ')
y = input('Hourly rate? ')
x = float(x)
y = float(y)
Pay = x * y
print('For' , x , 'hours of work at a rate of' ,y, 'per hour, you get:' ,Pay)
if Pay < 800:
    print('Get that bag up')
else:
    print('Big spender over here')
