#Using for loops to do all possible combinations
x = ['Brown', 'Black', 'Grey', 'White',]
y =['Tabby cat', 'German Shepherd', 'Beagle', 'American bulldog']
for i in x:
    for b in y:
        print(i, b)

#Find possible combinations for dog breeds and colors
count = 0
a1 = input('Pick a color:')
a2 = input('Pick another color:')
a3 = input('Pick a third color:')
b1 = input('Pick a breed:')
b2 = input('Pick another breed:')
b3 = input('Picka a third breed:')
Colors = [a1, a2, a3]
Breeds = [b1, b2, b3]
for i in Colors:
    for b in Breeds:
        count = count + 1
        print(count,i,b)