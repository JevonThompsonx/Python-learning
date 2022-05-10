for i in range(10,20):
    print(i)

x = 5
if x is not 2:
    print(x)

x = 5
if x is 2:
    print(x)
else: 
    print(' x is not 2')
y = 5 
def multiply():
    return (x * y)    
print(multiply())

o = input('Pleae enter a number: ')
p = input('Please enter a number: ')

try:
    o = float(o)
    p = float(p)
    print(o * p)

except: 
    print('Invalid input')    

word= 'I like cereal'
print(word[2:6])    

print(word.center(20,'6'))

wordplus= word.lower()
print(wordplus.count('i'))

if word.endswith('t'):
    print('It ends with t')
else:
    print('It does not end with t')
if word.startswith('I'):
    print('It starts with I')
else:
    print('It does not start with I')        