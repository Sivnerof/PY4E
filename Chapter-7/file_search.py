# 7.2 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# looking for lines of the form:
    # X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from 
# each of the lines and compute the average of those values and 
# produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when 
# you are testing below enter mbox-short.txt as the file name.


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "../Text-Files/mbox-short.txt"

try:
    fh = open(fname, 'r')
except:
    print('Could Not Open File')
    quit()

count = 0
spam_total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        spam_total += float(line[line.find(':') + 1:].strip())

print('Average spam confidence:', spam_total / count)