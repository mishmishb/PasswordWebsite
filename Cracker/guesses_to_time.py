''' Takes guesses as an input and convert these to time based on
different types of cracking. '''

def display_time(seconds):
    ''' Converts seconds into the most easily
    understandable time format. '''
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    months = days / 31
    years = months / 12

    if seconds < 60:
        readable_time = f'{round(seconds)} second'
    elif minutes < 60:
        readable_time = f'{round(minutes)} minute'
    elif hours < 24:
        readable_time = f'{round(hours)} hour'
    elif days < 31:
        readable_time = f'{round(days)} day'
    elif months < 12:
        readable_time = f'{round(months)} month'
    else:
        readable_time = f'{round(years)} year'

    if readable_time.split(' ')[0] != '1':
        readable_time += 's'

    return readable_time


def calc_time(guesses):
    ''' Takes the number of guesses and returns the amount of time
    it would take to make this many calculations based on different
    situations. 
    sourced from: https://github.com/dropbox/zxcvbn/blob/master/src/time_estimates.coffee 
    '''

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
