print('Recap time')
x = input('How many hours? ')
y = input('Hourly rate? ')
x = float(x)
y = float(y)
Pay = x * y
print('For' , x , 'hours of work at a rate of' ,y, 'per hour, you get:' ,Pay)
print('Good job. Now let us move on')

a = 25 * y
print(a)
if a > 400:
    print('It is greater than 400')
else:
    print('It is less than 400')
while a > 600:
    a = a - 20
    print(a)
    if a < 600:
        print('It is smaller than 600')
        quit()
while a < 600:
    a = a + 20
    print(a)
    if a > 600:
        print('It is bigger than 600')
        quit()