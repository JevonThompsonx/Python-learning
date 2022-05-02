l = 0
d = 0
sum = [ 800, 800,1000, 1500, 1500,300, 300,]
for x in sum:
    l = l + x
    d = d + 1
    print(d, l)
 #Using variables before the for loops seem to be what works best in using this type of loop
#Example:


#User inputted addition
count = 0
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
    count = count + i
    print(count)

#Another way to use the for loop is to check if a value is in a data set
# Example:

found = False
for i in [5, 9, 500,200, 100]:
    if i == 500:
        found = True
        print(i, "found it")
        break
    print(i,found)
if found == False :        
    print('Failed to find it')    


i = 25
while i > 15:
    print(i)
    i -= 1
  

    

tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)    

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')