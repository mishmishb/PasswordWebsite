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


def calc_time(guesses):

    online_throttled = display_time(guesses / (1 / 36))

    online_unthrottled = display_time(guesses / 1e1)

    offline_slow_hash = display_time(guesses / 1e4)

    offline_fast_hash = display_time(guesses / 1e10)

    times_to_crack = {'Throttled online attack': online_throttled, \
                      'Unthrottled online attack: ': online_unthrottled, \
                      'Slow hash offline attack: ': offline_slow_hash, \
                      'Fast hash  offline attack: ': offline_fast_hash
                      }

    return times_to_crack