from gettext import find


txt = 'Center'
txt = txt.center(20, "i")
print(txt)

x = [ 'Boy', 'Toy', 'Boy', 'Coy', 'Soy']

print(x.count("Boy"))

b = 0
for i in x:
    if i.endswith("y"):
        b +=1
    print(b)

for i in x:
    y = i.find("y")
    print(y)

x = [ 'Boy', 'Toy', 'Boy', 'Coy', 'Soy']

for i in x:
    a = input('Enter a string: ')
    if a == i:
        t = i.replace(i,'Got it') 
        print(t)
    else:
        "Wrong"
        continue