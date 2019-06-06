from frequency_lists import FREQUENCY_LISTS
from time import time
import itertools

RANKED_DICTIONARIES = {}

def produce_ranked_dict():
    
    def build_ranked_dict(ordered_list):
        return {word: idx for idx, word in enumerate(ordered_list, 1)}


    def add_frequency_lists(frequency_lists_):
        for name, lst in frequency_lists_.items():
            RANKED_DICTIONARIES[name] = build_ranked_dict(lst)
            
    add_frequency_lists(FREQUENCY_LISTS)
            
    return RANKED_DICTIONARIES


L33T_TABLE = {
    'a': ['4', '@'],
    'b': ['8'],
    'c': ['(', '{', '[', '<'],
    'e': ['3'],
    'g': ['6', '9'],
    'i': ['1', '!', '|'],
    'l': ['1', '|', '7'],
    'o': ['0'],
    's': ['$', '5'],
    't': ['+', '7'],
    'x': ['%'],
    'z': ['2'],
}

# omnimatch -- perform all matches
def omnimatch(password, _ranked_dictionaries=RANKED_DICTIONARIES):
    matches = []
    for matcher in [
        dictionary_match,
        my_l33t_match,
    ]:
        matches.extend(matcher(password, _ranked_dictionaries=_ranked_dictionaries))

    return sorted(matches, key=lambda x: (x['matched_length'], not x['l33t'], -x['rank']), reverse=True)

def dictionary_match(password, _ranked_dictionaries=RANKED_DICTIONARIES):
    matches = []
    length = len(password)
    password_lower = password.lower()
    for dictionary_name, ranked_dict in _ranked_dictionaries.items():
        for i in range(length):
            for j in range(i, length):
                if password_lower[i:j + 1] in ranked_dict:
                    word = password_lower[i:j + 1]
                    rank = ranked_dict[word]    
                    matches.append({
                        'pattern': 'dictionary',
                        'i': i,
                        'j': j,
                        'token': password[i:j + 1],
                        'matched_word': word,
                        'matched_length': len(word),
                        'rank': rank,
                        'dictionary_name': dictionary_name,
                        'l33t': False,
                    })

    return sorted(matches, key=lambda x: (x['i'], x['j']))


def alternative_l33t_table(password, table):
    password_chars = set(password)

    nonalpha = [a for a in password_chars if not a.isalpha()]

    #print(nonalpha)

    matches = {}
    for chr in nonalpha:
        #print('1:\t', chr)
        temp = [k for k, v in table.items() if chr in v]
        if temp:
            matches[chr] = temp

    return matches


def my_l33t_match(password, _ranked_dictionaries=RANKED_DICTIONARIES,
               _l33t_table=L33T_TABLE):

    matches = []

    my_l33t_table = alternative_l33t_table(password, _l33t_table)

    password_list = list(password)
    password_options = []
    for i in password_list:
        is_l33t = False
        for k,v in my_l33t_table.items():
            if k == i:
                password_options.append(v)
                is_l33t = True
                break
        if is_l33t == False:
            password_options.append(i)

    password_permutations = [''.join(perm) for perm in list(itertools.product(*password_options))]

    for permutation in password_permutations:
        for match in dictionary_match(permutation, _ranked_dictionaries):
            token = password[match['i']:match['j'] + 1]
            if token.lower() == match['matched_word']:
                continue

            # subset of mappings in sub that are in use for this match
            match_sub = {}
            for chr, letter in my_l33t_table.items():
                if chr in token: 
                    for lttr in letter:
                        if lttr in match['matched_word']:
                            match_sub[chr] = lttr
            match['l33t'] = True
            match['token'] = token
            match['sub'] = match_sub
            match['sub_display'] = ', '.join(
                ["%s -> %s" % (k, v) for k, v in match_sub.items()]
            )
            matches.append(match)

    matches = [match for match in matches if len(match['token']) > 1]

    return sorted(matches, key=lambda x: (x['i'], x['j']))


if __name__ == '__main__':

    inp = input('Password: ')

    start = time()
    
    print(omnimatch(inp, produce_ranked_dict()))
    
    end = time()

    print(end - start, 'seconds')
