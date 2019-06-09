''' Main module, contains function for collecting the strength results
and the function for running this and presenting the data. '''

from time import time

import word_extraction
import find_sequence
import calculate_guesses
import guesses_to_time
import advice


def mystrengthtool(input_password):
    ''' This function brings everything together. Each separate part
    of the program runs in order, sending the information necessary
    to each separate component, before returning the results we need.
    '''


    ranked_wordlists = word_extraction.dictionary_ranker()
    extracted_words = word_extraction.word_finder(input_password, ranked_wordlists)
    sequence = find_sequence.make_sequence(input_password, extracted_words)
    no_of_guesses = calculate_guesses.guess_calculator(sequence)
    password_advice = advice.advice_generator(input_password, sequence)
    ctime = guesses_to_time.calc_time(no_of_guesses)
    return [no_of_guesses, sequence, password_advice, ctime]



if __name__ == '__main__':

    PASSWORD = (input('Password: ')).replace(' ', '')

    START = time()

    RESULTS = mystrengthtool(PASSWORD)

    END = time()

    print('No of guesses:\t', RESULTS[0])
    print('Sequence:\t')
    for i in RESULTS[1]:
        print(i, '\n')

    print('Advice:\t')
    for k, v in RESULTS[2].items():
        print(k, v)

    print('ctime:\t')
    for k, v in RESULTS[3].items():
        print(k, v)


    print(END - START, 'seconds')
