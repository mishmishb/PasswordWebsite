''' Calculates the number of guesses required to crack the password
based on dictionary word ranks, uppercase and l33t swaps, and password
entropy for brute-force sections of the password. '''

from frequency_lists import FREQUENCY_LISTS

MALE_NAMES = len(FREQUENCY_LISTS['male_names'])
FEMALE_NAMES = len(FREQUENCY_LISTS['female_names'])
ENGLISH_WIKIPEDIA = len(FREQUENCY_LISTS['english_wikipedia'])
SURNAMES = len(FREQUENCY_LISTS['surnames'])
US_TV_AND_FILM = len(FREQUENCY_LISTS['us_tv_and_film'])
PASSWORDS = len(FREQUENCY_LISTS['passwords'])


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
        if match['pattern'] == 'dictionary':
            guesses *= dictionary_guess(match, match['dictionary_name'])
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

    sequence = match['token']

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

    brute_guess = round((search_space ** len(sequence)) / 2)

    return brute_guess



def dictionary_guess(match, dictionary_name):
    ''' Dictionary master function, checks which dictionary the word comes from,
    calculates any extra loops necessary due to checking for uppercase or l33t
    characters. '''

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
    ''' Checks each alpha character for uppercases and uses
    combinations to estimate how many extra loops through the
    dictionary it would check to find the word. '''

    word = match['token']

    if word.islower():
        return 0

    alpha_only = [chr for chr in word if chr.isalpha()]

    uppercase_count = 0

    for letter in alpha_only:
        if letter.isupper():
            uppercase_count += 1

    if (word[0].isupper() and uppercase_count == 1) or word.isupper():
        return 1

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

    token_lower = match['token'].lower()
    if token_lower == match['matched_word']:
        return 0

    dictionary_loops = 1

    for l33t, original in match['sub'].items():
        l33t_count = token_lower.count(l33t)
        original_count = sum(token_lower.count(o) for o in original)

        if 0 in (l33t_count, original_count):
            dictionary_loops *= 2
        else:
            potential_swaps = 0
            for i in range(1, min(l33t_count, original_count) + 1):
                potential_swaps += combination_count(l33t_count + original_count, i)
            dictionary_loops *= potential_swaps

    return dictionary_loops
