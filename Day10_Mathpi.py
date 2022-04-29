l = 0
d = 0
sum = [ 800, 800,1000, 1500, 1500,300, 300,]
for x in sum:
    l = l + x
    d = d + 1
    print(d, l)
 #Using variables before the for loops seem to be what works best in using this type of loop
#Example:

#Create a for loop that subtracts the variables from each other variable
count = 0
x = input('Enter the first variable: ')
y = input('Enter the second variable: ')
z = input('Enter the third variable: ')
w = input('Enter the fourth variable: ')
x= float(x)
y= float(y)
z= float(z)
w= float(w)
subs = [ x, y , z , w  ]
for i in subs:
    if count == 0:   
        count = i
        continue
    count= i - count
    print(count)

#Another way to use the for loop is to check if a value is in a data set
# Example:

