import os
import sys

if len(sys.argv) < 2:
    print('You need to specify int value for range upto with the table need to be printed as an argument')
    sys.exit()

input_range = sys.argv[1]

input_range = int(input_range)

#To get the table excluding element divible by 5.
result_table =  [n * 3 for n in range(1, input_range) if n % 5 != 0]


print(result_table)
