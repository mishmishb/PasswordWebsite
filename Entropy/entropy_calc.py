import math
import getpass
import re
import time

def ez_format(guesses):

    guesses_format = "{:,}".format(guesses)
    return guesses_format
    
def display_time(seconds):
    minute = 60
    hour = minute * 60
    day = hour * 24
    month = day * 31
    year = month * 12
    century = year * 100
    if seconds < 1:
         display_num, display_str = seconds, '%s seconds' % seconds
    if seconds < minute:
        base = round(seconds)
        display_num, display_str = base, '%s second' % base
    elif seconds < hour:
        base = round(seconds / minute)
        display_num, display_str = base, '%s minute' % base
    elif seconds < day:
        base = round(seconds / hour)
        display_num, display_str = base, '%s hour' % base
    elif seconds < month:
        base = round(seconds / day)
        display_num, display_str = base, '%s day' % base
    elif seconds < year:
        base = round(seconds / month)
        display_num, display_str = base, '%s month' % base
    elif seconds < century:
        base = round(seconds / year)
        display_num, display_str = base, '%s year' % base
    else:
        display_num, display_str = None, 'centuries'

    if display_num and display_num != 1:
        display_str += 's'

    return display_str

def entropy():

    set_size = 0

    inp = input('Password:')

    start = time.time()

    if re.search('[a-z]', inp):
        set_size += 26

    if re.search('[A-Z]', inp):
        set_size += 26

    if re.search('\d', inp):
        set_size += 10

    if re.search('./<>?;:"\'`!@#$%^&*()\[\]{}_+=|\\-', inp):
        set_size += 33

    length = len(inp)

    entropy = math.log2(set_size ** length)

    guesses = (2 ** entropy) / 2
    
    total_guesses = ez_format(guesses)

    online_throttled = display_time(guesses / (1 / 36))

    online_unthrottled = display_time(guesses / 1e1)

    offline_slow_hash = display_time(guesses / 1e4)

    offline_fast_hash = display_time(guesses / 1e10)

    end = time.time()

    run_time = end - start

    print("######################################")
    print("### Set size: ", set_size)
    print("### Password length: ", length)
    print("### Entropy: ", entropy)
    print("### Average number of guesses for this password: ", total_guesses)
    print("### Guess times :")
    print("### \t Throttled online attack: ", online_throttled)
    print("### \t Unthrottled online attack: ", online_unthrottled)
    print("### \t Slow hash offline attack: ", offline_slow_hash)
    print("### \t Fast hash  offline attack: ", offline_fast_hash)
    print("This took ", run_time, " seconds to calculate")
    print("######################################")
    
    
if __name__ == "__main__":
    entropy()
    
    
