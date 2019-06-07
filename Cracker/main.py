''' Main module, contains function for collecting the strength results
and the function for running this and presenting the data. '''

from time import time

import mymatching
import mysearch
import guesses
import guesses_to_time


def mystrengthtool(input_password):
    ''' This function brings everything together. Each separate part
    of the program runs in order, sending the information necessary
    to each separate component, before returning the results we need.
    '''


    ranked_dictionaries = mymatching.produce_ranked_dict()
    matches = mymatching.omnimatch(input_password, ranked_dictionaries)
    sequence = mysearch.search(input_password, matches)
    no_of_guesses = guesses.guess_calculator(sequence)
    ctime = guesses_to_time.calc_time(no_of_guesses)
    return [no_of_guesses, sequence, ctime]



if __name__ == '__main__':

    PASSWORD = input('Password: ')

    START = time()

    RESULTS = mystrengthtool(PASSWORD)

    END = time()

    print('No of guesses:\t', RESULTS[0])
    print('Sequence:\t')
    for i in RESULTS[1]:
        print(i, '\n')

    print('ctime:\t')
    for k, v in RESULTS[2].items():
        print(k, v)


    print(END - START, 'seconds')
