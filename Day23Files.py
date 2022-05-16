#Count these lines and extract the floating point values from each of the lines and compute the average 
# of those values and produce an output as shown below. Do not use the sum() 
# function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing
#  below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a = line.find(':')
    data = line[a + 1:]
    data = float(data)
    count += 1
    average += data
    
print("Average spam confidence:" , average/count)

