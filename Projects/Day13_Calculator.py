while True:
    o = input('Ready to calculate? ')
    if o == 'no' or o == 'No':
        break
    elif o == 'Yes' or o == 'yes':
        def calc(b):
            if b == 'Add':
                print(x2 + y2)
            if b == 'Subtract':
                print(x2 - y2)
            if b == 'Multiply2':    
                print(x2 * y2)
            if b == 'Divide':
                print(x2/y2)

        x = input('Enter the first number: ')
        print('''        Add
        Subtract
        Multiply
        Divide''')
        a = input('Enter the arithmetic from the list:')
        y = input('Enter the second number: ' )
        x2 = float(x)
        y2 = float(y)


        if a == 'Add':
            calc('Add')
        elif a == 'Multiply':
            calc('Multiply')
        elif a == 'Divide':
            calc('Divide')
        elif a == 'Subtract':
            calc('Subtract')    
        else:
            print('Invalid')    
            continue     
    else:
        continue    
print('All done')    