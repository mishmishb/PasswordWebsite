import math
import getpass
import re
import time

set_size = 0

inp = getpass.getpass()

start = time.time()

if re.search('[a-z]', inp):
    set_size += 26

if re.search('[A-Z]', inp):
    set_size += 26

if re.search('\d', inp):
    set_size += 10

if re.search('/[$-/:-?{-~!"^_`\[\]]/', inp):
    set_size += 29

length = len(inp)

entropy = length * math.log2(set_size)

guesses = (2 ** entropy) / 2

ez_format = "{:,}".format(guesses)

end = time.time()

run_time = end - start

print("Set size: ", set_size)
print("Average number of guesses for this password would be: ", ez_format)
print("This took ", run_time, " seconds to calculate")
