from time import time

import mymatching, mysearch

def mystrengthtool(password):

    start = time()
    
    ranked_dictionaries = mymatching.produce_ranked_dict()
    matches = mymatching.omnimatch(password, ranked_dictionaries)
    sequence = mysearch.search(password, matches)
    
    end = time()

    print(sequence)
    print(end - start, 'seconds')
    
   
if __name__ == '__main__':
    
    password = input('Password: ')
    
    mystrengthtool(password)
