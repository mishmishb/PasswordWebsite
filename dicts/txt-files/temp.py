import os
from time import time

start = time()
bum = 'sdfsdfsadfasdf'
files = os.listdir('.')
total_num_lines = 0
for i in files:
    with open(i, 'r') as f:
        file_num_lines = 0
        for line in f:
            total_num_lines += 1
            file_num_lines += 1
    print('File:', i, 'Lines: ', file_num_lines)
print('Total lines:', total_num_lines)
end = time()
time_taken = end - start
print(time_taken, 'seconds')
