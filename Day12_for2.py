#Keep only the largest value in the list
b =0
count = 0
x = [5,20, 9, 200,22, 89,99,101]
for i in x:
    if i > b:
        b = i
    print(i,b)
    count += 1
print( b, 'Is the largest value in this set')
print(b/count, 'Is the average')
# Perfect

#Filtering for loops
a = 0
y = [50, 100,322, 200, 300, 50, 25, 69]
print('''These are all the numbers in 
the set that are greater than 100''')
for b in y:
    if b >= 100:
        print(b)

a = False
c = [22, 23, 24, 25, 26, 27, 28, 29, 30]
for l in c:
    if l==25:
        a = True
        print(l ,'Found it')
        break
    print(l,a)    

#User inputted subtraction
count = None
x = input('Enter the first variable: ')
y = input('Enter the second variable: ')
z = input('Enter the third variable: ')
w = input('Enter the fourth variable: ')
x= float(x)
w= float(w)
y= float(y)
z= float(z)
subs = [ x, y , z , w  ]
for i in subs:
    if count == None:
        count = i
        continue
    count = count - i
    print(count)