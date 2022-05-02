largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum =int(num)
    except:
        print("Invalid input")
    if largest == None:
        largest = fnum
        smallest = fnum
    elif fnum > largest:
        largest = fnum
    elif fnum < smallest:
        smallest = fnum
print("Maximum is", largest)
print("Minimum is", smallest)