x = 'Tomato'
print(x[3:5])

y = list()
y.append(5)
y.append(9)
y.append(22)
y.append(3)
y.sort()
print(y)

print(max(y))
print(min(y))
print(sum(y))
print(len(y))
print(sum(y)/len(y))

if 22 in y:
    print(True)
o = [29, 100, 500]
print(o)
a = o + y
print(a)
    
count = 0
name = 'My name is Jevon Thompson'
sname = name.split()
for x in sname:
    count += 1
    if x == 'Jevon':
        print('Found it!', 'It is in the', count, 'position')

num_list = ('4;9;0;1;2;3;4;5')
num_list.split(';')
for x in num_list:
    if x == ';':
        continue
    print(x)

o = [29, 100, 500]

print(o)

