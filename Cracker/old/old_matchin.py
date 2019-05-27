from time import time

from getpass import getpass
from frequency_lists import FREQUENCY_LISTS


def build_ranked_dict(ordered_list):
        return {word: idx for idx, word in enumerate(ordered_list, 1)}
        
        
def add_frequency_lists(frequency_lists_):
    RANKED_DICTIONARIES = {}
    for name, lst in frequency_lists_.items():
        RANKED_DICTIONARIES[name] = build_ranked_dict(lst)
    return RANKED_DICTIONARIES
            
            
def dictionary_match(pw, ranked_wordlist):
        result = []
        length = len(pw)
        for dictionary_name, ranked_dict in ranked_wordlist.items():
            for i in range(length):
                for j in range(i, length):
                    if pw[i:j+1] in ranked_dict:
                        word = pw[i:j+1]
                        word_length = len(word)
                        rank = ranked_dict[word]
                        result.append({
                            'pattern': 'dictionary',
                            'dictionary': dictionary_name,
                            'match': word,
                            'rank': rank,
                            'i': i,
                            'j': j,
                            'length': word_length
                            })

        return sorted(result, reverse=True, key=lambda x: (x['length'])) 
            
            
def main():

    pw = getpass()

    start = time()
    
    RANKED_DICTIONARIES = add_frequency_lists(FREQUENCY_LISTS)
    output = dictionary_match(pw, RANKED_DICTIONARIES)

    print(output)

    end = time()
    print('This took', end - start, 'seconds')

if __name__ == '__main__':
    main()

