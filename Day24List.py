List = [ ' Bob', 'Joshua', 'Joseph', 'Jessica', ' John', 'Bethany']
x = ['Sarah', 25, 90.75]
print(x)
y = [25, 90.75, 70,[90, 70, 70], 100]
print(y)

#lists can be used to run through each value in the list and write clean code
dogs = ['Sandy', 'Simba','Cookie','Onix']

for i in dogs:
    print('Good morning,' ,i )
#Loops through each name one by one    
#Lists can be selected from using brackets like slicing strings
#Starts from 0
print( 'Good morning,' ,dogs[2] )

#Lists are mutable-changable

dogs = ['Sandy', 'Simba','Cookie','Onix']
print(dogs)
Number = input('Select a number to replace: ')
Number = int(Number)
Name = input('select the new name: ')

dogs[Number] = Name

print(dogs)

#Len counts the anount of items in a lists
print(len(dogs))

print(range(len(dogs)))

pets = ['Simba', 'Kat', 'Cookie']

for i in range(len(pets)):
    x = input('Enter a name:')
    pets[i] = x
print(pets)