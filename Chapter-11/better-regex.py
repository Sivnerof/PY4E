# Python 3:
    # import re
    # print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

    # ../Text-Files/regex_sum_42.txt
    # ../Text-Files/regex_sum_1495646.txt

import re

print([ re.findall('[0-9]+', line.strip()) for line in open('../Text-Files/regex_sum_42.txt') if re.findall('[0-9]+', line)])


#result = []
#for line in fh:
#    if re.findall('[0-9]+', line.strip()):
#        result.append(re.findall('[0-9]+', line.strip()))

#item_sum = 0
#for items in result:
#    for item in items:
#        item_sum += int(item)

#print(item_sum)