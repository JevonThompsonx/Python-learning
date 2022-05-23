#Prompt:
#Open the file romeo.txt and read it line by line. 
#For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. 
#For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    li_st = line.split()
    for i in li_st:
        if i == ' ' or i in lst:
            continue
        else:
            lst.append(i)
lst.sort()            
print(lst)

#data:
#But soft what light through yonder window breaks
#It is the east and Juliet is the sun
#Arise fair sun and kill the envious moon
#Who is already sick and pale with grief
