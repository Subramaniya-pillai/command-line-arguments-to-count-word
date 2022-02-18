'''Developed by: Subramaniya pillai.B
   Reference No: 21006076'''

import sys
count=0
with open(sys.argv[1], 'r') as f:
    for line in f:
        word=line.split()
        count += len(word)
print("No. of words in the file:",count)