#Remaking my anime recommendation list that wont crash when an invalid number is entered
def animelist(anime):
    if anime == 'DS':
        print('Demon slayer')
    if anime == 'N':
        print('Naruto')
    if anime == 'Bl':
        print('Bleach')
    if anime == 'Ju':
        print('Jujutsu')
    if anime == 'Liw':
        print('Love is war')
    if anime == 'Aot':
        print('Attack on titan')


while True:
    x = input('Pick a number between 1 and 100: ')
    x = float(x)
    if x <= 100 and x >= 80:
        animelist('DS')
        break
    elif x <= 80 and x >= 60:
        animelist('N')
        break
    elif x <= 60 and x >= 40:
        animelist('Ju')
        break
    elif x <= 40 and x >= 20:
        animelist('Aot')
        break
    elif x <= 20 and x >= 10:
        animelist('Bl')
        break
    elif x <= 10 and x >= 0:
        animelist('Liw')
        break
    else:
        print('Please elect a valid number')
        continue

            

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly.
#Remaking without error of using inputting 0

hrs = input("Enter Hours: ")
h = float(hrs)

rate = input('Rate: ')
r = float(rate)
while True: 
    if rate == 'done' or rate == 'Done':
        break
    elif h > 40.0:
        x = (h - 40.0) * (r * 1.5) + (40 * r)
        continue
    elif r == 0 or h == 0:
        print('Please enter valid numbers')
        continue
    else:
        x = r * h
        continue
    print(x)

