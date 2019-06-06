from time import time

import mymatching, mysearch, guesses, guesses_to_time

def mystrengthtool(password):

    
    
    ranked_dictionaries = mymatching.produce_ranked_dict()
    matches = mymatching.omnimatch(password, ranked_dictionaries)
    print(matches)
    sequence = mysearch.search(password, matches)
    no_of_guesses = guesses.guess_calculator(sequence)
    ctime = guesses_to_time.calc_time(no_of_guesses)
    return [no_of_guesses, sequence, ctime]
    
    
   
if __name__ == '__main__':
    
    password = input('Password: ')

    start = time()

    results = mystrengthtool(password)

    end = time()

    print('No of guesses:\t', results[0])
    print('Sequence:\t')
    for i in results[1]:
    	print(i, '\n')

    print('ctime:\t')
    for k,v in results[2].items():
    	print(k, v)


    print(end - start, 'seconds')
