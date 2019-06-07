''' This module compares sections of the password against the dictionaries
provided to find the different sequences of words, and brute-force strings,
as well as detecting instances of l33t subsitition.
'''

import itertools

from frequency_lists import FREQUENCY_LISTS


RANKED_DICTIONARIES = {}

def produce_ranked_dict():
    ''' Takes the frequency_list.py file as input and generates a dictionary
    from this file with rankings for each word'''

    for dictionary_name, dictionary_words in FREQUENCY_LISTS.items():
        RANKED_DICTIONARIES[dictionary_name] = \
        {word: rank for rank, word in enumerate(dictionary_words, 1)}

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
def omnimatch(password, ranked_dictionaries):
    '''Used for implementing dictionary_match and my_l33t_match'''

    matches = []
    for matcher in [dictionary_match, my_l33t_match]:
        matches.extend(matcher(password, ranked_dictionaries=ranked_dictionaries))

    return sorted(matches,
                  key=lambda x: (x['matched_length'], not x['l33t'], -x['rank']), reverse=True)

def dictionary_match(password, ranked_dictionaries):
    ''' Checks through each character of the inputted password to find
    sequences that contain words found in the dictionaries'''

    matches = []
    length = len(password)
    password_lower = password.lower()
    for dictionary_name, ranked_dict in ranked_dictionaries.items():
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

    return matches


def generate_l33t_table(password, table):
    ''' Inspects the non-alpha characters in the password and returns a list of
    letteres for potential character swaps'''

    password_chars = set(password)

    nonalpha = [a for a in password_chars if not a.isalpha()]

    matches = {}
    for n_a in nonalpha:
        temp = [k for k, v in table.items() if n_a in v]
        if temp:
            matches[n_a] = temp

    return matches


def my_l33t_match(password, ranked_dictionaries):
    ''' Performs l33t matches, '''

    matches = []

    my_l33t_table = generate_l33t_table(password, L33T_TABLE)

    password_list = list(password)
    password_options = []
    for i in password_list:
        is_l33t = False
        for l33t, letter in my_l33t_table.items():
            if l33t == i:
                password_options.append(letter)
                is_l33t = True
                break
        if is_l33t is False:
            password_options.append(i)

    password_permutations = [''.join(perm) for perm in list(itertools.product(*password_options))]

    for permutation in password_permutations:
        for match in dictionary_match(permutation, ranked_dictionaries):
            if match['matched_length'] > 1:
                token = password[match['i']:match['j'] + 1]
                if token.lower() == match['matched_word']:
                    continue

                match_sub = {}
                for l33t, letter in my_l33t_table.items():
                    if l33t in token:
                        match_sub[l33t] = [lttr for lttr in letter if lttr in match['matched_word']]
                match['l33t'] = True
                match['token'] = token
                match['sub'] = match_sub
                matches.append(match)

    return matches
