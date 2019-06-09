''' This module compares sections of the password against the
dictionaries provided to find the different sequences of words,
and brute-force strings, as well as detecting instances of l33t
subsitition. '''

import itertools

from data import FREQUENCY_LISTS, L33T_CHARACTERS


RANKED_WORDLISTS = {}

def dictionary_ranker():
    ''' Takes the frequency_list.py file as input and generates a
    dictionary from this file with rankings for each word. '''

    for name, dictionary_words in FREQUENCY_LISTS.items():
        # For each wordlist creates a key where the value is a dictionary
        # of the words from that list, with their corresponding rank.
        RANKED_WORDLISTS[name] = \
        {word: rank for rank, word in enumerate(dictionary_words, 1)}

    return RANKED_WORDLISTS


def word_finder(password, ranked_wordlists):
    '''Used for implementing dictionary_finder and l33t_finder'''

    found_words = []
    for finder in [dictionary_finder, l33t_finder]:
        # Collects a list of each different word found, including those using
        # 'l33t speak'.
        found_words.extend(finder(password, ranked_wordlists))

    return sorted(found_words,
                  key=lambda x: (
                      x['length'], not x['l33t'], -x['rank']), reverse=True
                  )

def dictionary_finder(password, ranked_wordlists):
    ''' Checks through each character of the inputted password to find
    sequences that contain words found in the dictionaries'''

    found_words = []
    length = len(password)
    password_lower = password.lower()

    # For each dictionary, checks each contiguous substring
    # for a match and returns some relevant information.
    for name, word_list in ranked_wordlists.items():
        for start in range(length):
            for end in range(start, length):
                if password_lower[start:end + 1] in word_list:
                    word = password_lower[start:end + 1]
                    rank = word_list[word]
                    found_words.append({
                        'start': start,
                        'end': end,
                        'pattern_type': 'dictionary',
                        'input': password[start:end + 1],
                        'length': len(word),
                        'word_list': name,
                        'found_word': word,
                        'rank': rank,
                        'l33t': False,
                    })

    return found_words


def generate_l33t_list(password, l33t_list):
    ''' Inspects the non-alpha characters in the password and returns a list of
    letters for potential character swaps'''

    # Filters out letters from password.
    nonalpha = [a for a in password if not a.isalpha()]


    swaps = {}
    for n_a in nonalpha:
        # Creates list of letters that might have been swapped
        # for a non-alpha character.
        swapped_letters = [
            lettrs for lettrs, l33ts in l33t_list.items() if n_a in l33ts
            ]
        if swapped_letters:
            swaps[n_a] = swapped_letters

    # Returns dictionary of the non-alpha characters and their
    # corresponding letters as per l33t_list.
    return swaps


def l33t_finder(password, ranked_wordlists):
    ''' Swaps out potential l33t characters with letters and checks
    each permutation against the dictionary. '''

    found_words = []

    # Generates l33t list from password string.
    l33t_list = generate_l33t_list(password, L33T_CHARACTERS)
    
    # Generates a list with potential swaps grouped together.
    # e.g. te5t -> ['t', 'e', ['s', 'z'], 't']
    password_options = []
    for position, value in enumerate(password):
        is_l33t = False
        for l33t, letter in l33t_list.items():
            if l33t == value:
                password_options.append(letter)
                is_l33t = True
                break
        if is_l33t is False:
            password_options.append(value)

    # From the list of options, creates a list of the different potential
    # outcomes so that they can all be checked against a dictionary.
    # e.g. ['test', 'tezt']
    password_permutations = [
        ''.join(perm) for perm in list(itertools.product(*password_options))
        ]

    for permutation in password_permutations:
        for word in dictionary_finder(permutation, ranked_wordlists):
            # It isn't worth l33t swapping single characters, these
            # are better off being brute-forced.
            if word['length'] > 1:
                sequence = password[word['start']:word['end'] + 1]
                # If the sequence doesn't contain any l33t swaps, skip it.
                if sequence.lower() == word['found_word']:
                    continue

                swap = {}
                for l33t, letter in l33t_list.items():
                    swap_list = []
                    if l33t in sequence:
                        for l in letter:
                            if l not in sequence:
                                swap_list.extend(l)
                        if swap_list:
                            swap[l33t] = swap_list
                word['l33t'] = True
                word['input'] = sequence
                word['swap'] = swap
                found_words.append(word)

    return found_words
