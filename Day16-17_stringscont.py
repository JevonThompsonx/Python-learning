#Wordle
b = 0
y = 0
x = [ 'Boy', 'Toy', 'Joy', 'Coy', 'Soy']
x2 = x
for a in x2:
    y += 1
while True:
    a = input('Enter five 3 letter word that rhymes with "Enjoy" : ')
    if a in x:
        print('Correct')
        x[b]= False
        b += 1
        if b == y:
            break
    else: 
        print('Invalid')    
print('All done')    

o = 'Jack'
j = o.lower()
while True:
    print('The word is', o)
    a = input('Enter a word:')
    a = a.lower()
    if a > j:
        print('Your word', a , 'is greater than', o)
    elif a < j:
        print('Your word', a, 'is less than', o )
    elif a == j:
        print('Try again')
        continue
