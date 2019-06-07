import math

MALE_NAMES = 1219
FEMALE_NAMES = 4275
ENGLISH_WIKIPEDIA = 100000
SURNAMES = 88799
US_TV_AND_FILM = 39070
PASSWORDS = 47023


def nCk(n, r):

    r = min(r, n-r)
    if r == 0: return 1
    res = 1
    for k in range(1,r+1):
        res = res*(n-k+1)/k
    return res

def guess_calculator(password):

    guesses = 1
    for match in password:
        if match['pattern'] == 'dictionary':
            guesses *= dictionary_guess(match, match['dictionary_name'])
        else:
            guesses *= bruteforce_guesses(match)

    return guesses



def bruteforce_guesses(match):
    low_alpha = False
    upper_alpha = False
    number = False
    symbol = False
    potential_symbols = '!"£$€%^&*()-_=+[]{}#~\'@/?.>,<|\`¬'
    search_space = 0

    sequence = match['token']

    for chr in sequence:
        if (chr.islower() and low_alpha == False):
            search_space += 26
            low_alpha = True
        elif (chr.isupper() and upper_alpha == False):
            search_space += 26
            upper_alpha = True
        elif (chr.isdecimal() and number == False):
            search_space += 10
            number = True
        elif(chr in potential_symbols and symbol == False):
            search_space += 33
            symbol = True

    brute_guess = round((search_space ** len(sequence)) / 2)

    return brute_guess



def dictionary_guess(match, dictionary_name):

    if dictionary_name == 'passwords':
        dictionary_length = PASSWORDS
    elif dictionary_name == 'english_wikipedia':
        dictionary_length = ENGLISH_WIKIPEDIA 
    elif dictionary_name == 'us_tv_and_film':
        dictionary_length = US_TV_AND_FILM
    elif dictionary_name == 'male_names':
        dictionary_length = MALE_NAMES
    elif dictionary_name == 'female_names':
        dictionary_length = FEMALE_NAMES
    elif dictionary_name == 'surnames':
        dictionary_length = SURNAMES

    upper_loops = uppercase_character_loops(match)
    l33t_loops = l33t_character_loops(match)

    guesses = match['rank'] + (dictionary_length * upper_loops) \
                            + (dictionary_length * l33t_loops)

    return guesses


def uppercase_character_loops(match):

    word = match['token']

    if word.islower():
        return 0

    alpha_only = [chr for chr in word if chr.isalpha()]

    uppercase_count = 0
    lowercase_count = 0

    for letter in alpha_only:
        if letter.isupper():
            uppercase_count += 1

    if (word[0].isupper() and uppercase_count == 1) or word.isupper():
        return 1
    
    dictionary_loops = 0
    for k in range(1, uppercase_count + 1):
        if k == uppercase_count:
            dictionary_loops += (nCk(len(alpha_only), k) / 2)
        else:
            dictionary_loops += nCk(len(alpha_only), k)

    return dictionary_loops


def l33t_character_loops(match):
    token_lower = match['token'].lower()
    if token_lower == match['matched_word']:
        return 0

    dictionary_loops = 1

    for l33t, original in match['sub'].items():
        l33t_count = token_lower.count(l33t)
        original_count = token_lower.count(original)

        if 0 in (l33t_count, original_count):
            dictionary_loops *= 2
        else:
            potential_swaps = 0
            for i in range(1, min(l33t_count, original_count) + 1):
                potential_swaps += nCk(l33t_count + original_count, i)
            dictionary_loops *= potential_swaps

    return dictionary_loops





