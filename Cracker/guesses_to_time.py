''' Takes guesses as an input and convert these to time based on
different types of cracking. '''

def display_time(seconds):
    ''' Takes seconds as input and converts this to a string based
    on the number of seconds. '''

    minute = 60
    hour = 3600
    day = 86400
    month = 2678400
    year = 32140800
    if seconds < minute:
        rounded = round(seconds)
        display_str = f'{rounded} second'
    elif seconds < hour:
        rounded = round(seconds / minute)
        display_str = f'{rounded} minute'
    elif seconds < day:
        rounded = round(seconds / hour)
        display_str = f'{rounded} hour'
    elif seconds < month:
        rounded = round(seconds / day)
        display_str = f'{rounded} day'
    elif seconds < year:
        rounded = round(seconds / month)
        display_str = f'{rounded} month'
    else:
        rounded = round(seconds / year)
        display_str = f'{rounded} year'

    if display_str.split(' ')[0] != '0':
        display_str += 's'

    return display_str


def calc_time(guesses):
    ''' Takes the number of guesses and returns the amount of time
    it would take to make this many calculations based on different
    situations. '''

    online_throttled = display_time(guesses / (1 / 36))

    online_unthrottled = display_time(guesses / 1e1)

    offline_slow_hash = display_time(guesses / 1e4)

    offline_fast_hash = display_time(guesses / 1e10)

    times_to_crack = {'Throttled online attack:\t': online_throttled, \
                      'Unthrottled online attack:\t': online_unthrottled, \
                      'Slow hash offline attack:\t': offline_slow_hash, \
                      'Fast hash  offline attack:\t': offline_fast_hash
                     }

    return times_to_crack
