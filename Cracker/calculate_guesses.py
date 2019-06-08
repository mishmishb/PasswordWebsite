''' Calculates the number of guesses required to crack the password
based on dictionary word ranks, uppercase and l33t swaps, and password
entropy for brute-force sections of the password. '''

from data import FREQUENCY_LISTS, L33T_CHARACTERS

def combination_count(n, r):
    ''' Efficient combinations counter from https://stackoverflow.com/a/44600243 '''

    r = min(r, n-r)
    if r == 0:
        return 1
    res = 1
    for k in range(1, r + 1):
        res = res * (n - k + 1) / k
    return res

def guess_calculator(password):
    ''' Guesses master function, combines dictionary results with
    bruteforce results. '''

    guesses = 1
    for match in password:
        if match['pattern_type'] == 'dictionary':
            guesses *= dictionary_guess(match, match['word_list'])
        else:
            guesses *= bruteforce_guesses(match)

    return guesses



def bruteforce_guesses(match):
    ''' Works out which sets are involved in the word and performs an entropy
    calculation based on https://www.pleacher.com/mp/mlessons/algebra/entropy.html
    The entropy step is skipped as we just need the number of guesses. '''

    low_alpha = False
    upper_alpha = False
    number = False
    symbol = False
    potential_symbols = r'!"£$€%^&*()-_=+[]{}#~\'@/?.>,<|`¬'
    search_space = 0

    sequence = match['input']

    # Checks what character sets are in the string
    for character in sequence:
        if (character.islower() and low_alpha is False):
            search_space += 26
            low_alpha = True
        elif (character.isupper() and upper_alpha is False):
            search_space += 26
            upper_alpha = True
        elif (character.isdecimal() and number is False):
            search_space += 10
            number = True
        elif(character in potential_symbols and symbol is False):
            search_space += 33
            symbol = True

    # See function doc string
    brute_guess = round((search_space ** len(sequence)) / 2)

    return brute_guess



def dictionary_guess(match, dictionary_name):
    ''' Dictionary master function, checks which dictionary the word comes from,
    calculates any extra loops necessary due to checking for uppercase or l33t
    characters. '''

    dictionary_length = len(FREQUENCY_LISTS[dictionary_name])

    # Calculates any extra loops needed for uppercase or l33t characters
    upper_loops = uppercase_character_loops(match)
    l33t_loops = l33t_character_loops(match)

    guesses = match['rank'] + (dictionary_length * upper_loops) \
                            + (dictionary_length * l33t_loops)

    return guesses


def uppercase_character_loops(match):
    ''' Checks each alpha character for uppercases and uses
    combinations to estimate how many extra loops through the
    dictionary it would check to find the word. '''

    word = match['input']

    # If the word countains no capital letters, return
    if word.islower():
        return 0

    # Extracts alpha characters
    alpha_only = [a for a in word if a.isalpha()]

    # Counts uppercase characters
    uppercase_count = 0
    for letter in alpha_only:
        if letter.isupper():
            uppercase_count += 1

    # First check, after original, would be first letter Upper or all UPPER
    if (word[0].isupper() and uppercase_count == 1) or word.isupper():
        return 1

    # Calculates loops based on needing to test all positions for
    # previous number of capital letters
    # e.g. to check for 2 capital letters, would need to check all
    # positions for one capital letter, followed by half of the
    # positions for 2 capital letters (on average)
    dictionary_loops = 0
    for k in range(1, uppercase_count + 1):
        if k == uppercase_count:
            dictionary_loops += (combination_count(len(alpha_only), k) / 2)
        else:
            dictionary_loops += combination_count(len(alpha_only), k)

    return dictionary_loops


def l33t_character_loops(match):
    ''' Calculates the number of extra loops through the dictionaries
    are necessary for the amount of swaps in the word. '''

    token_lower = match['input'].lower()

    # If input (ignoring case) matches the dictionary word, return
    if token_lower == match['found_word']:
        return 0

    # Extracts alpha characters
    alpha_only = [a for a in token_lower if a.isalpha()]

    # Counts the number of characters in the word that either are already l33ted,
    # or could be l33ted, to figure out how many permutations of l33ts the
    # word has
    potential_swaps = len([l for l in alpha_only if l in L33T_CHARACTERS.keys()]) \
                    + len(match['swap'])

    # Once number of potential permutations for each word has been calculated
    # figures out how many times the tool would need to loop through the
    # dictionaries to find the right combination
    dictionary_loops = 0
    for k in range(1, len(match['swap']) + 1):
        if k == potential_swaps:
            dictionary_loops += (combination_count(potential_swaps, k) / 2)
        else:
            dictionary_loops += combination_count(potential_swaps, k)

    return dictionary_loops
