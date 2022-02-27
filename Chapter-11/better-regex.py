# ../Text-Files/regex_sum_42.txt
# ../Text-Files/regex_sum_1495646.txt

import re

print(sum([int(num) for num in re.findall('[0-9]+', open('../Text-Files/regex_sum_42.txt').read())]))