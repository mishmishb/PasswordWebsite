import math

MALE_NAMES = 1219
FEMALE_NAMES = 4275
ENGLISH_WIKIPEDIA = 100000
SURNAMES = 88799
US_TV_AND_FILM = 39070
PASSWORDS = 47023


def nCk(n, k):
    """http://blog.plover.com/math/choose.html"""
    if k > n:
        return 0
    if k == 0:
        return 1

    r = 1
    for d in range(1, k + 1):
        r *= n
        r /= d
        n -= 1

    return r

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

    if (word[0].isupper() and uppercase_count == 1):
        return 1
    
    if ((word[-1].isupper() and uppercase_count == 1) or word.isupper()):
        return 2.5

    dictionary_loops = 0
    for k in range(1, uppercase_count + 1):
        if k == uppercase_count:
            dictionary_loops += (nCk(len(alpha_only), k) / 2)
        else:
            dictionary_loops += nCk(len(alpha_only), k)

    return dictionary_loops


def l33t_character_loops(match):
    if match['token'].lower() == match['matched_word']:
        return 0

    variations = 1

    for subbed, unsubbed in match['sub'].items():
        # lower-case match.token before calculating: capitalization shouldn't
        # affect l33t calc.
        chrs = list(match['token'].lower())
        S = sum(1 for chr in chrs if chr == subbed)
        U = sum(1 for chr in chrs if chr == unsubbed)
        if S == 0 or U == 0:
            # for this sub, password is either fully subbed (444) or fully
            # unsubbed (aaa) treat that as doubling the space (attacker needs
            # to try fully subbed chars in addition to unsubbed.)
            variations *= 2
        else:
            # this case is similar to capitalization:
            # with aa44a, U = 3, S = 2, attacker needs to try unsubbed + one
            # sub + two subs
            p = min(U, S)
            possibilities = 0
            for i in range(1, p + 1):
                possibilities += nCk(U + S, i)
            variations *= possibilities

    return variations



if __name__ == '__main__':


    #print(l33t_character_guesses({'pattern': 'dictionary', 'i': 3, 'j': 7, 'token': 'L3m0n', 'matched_word': 'lemon', 'matched_length': 5, 'rank': 1686, 'dictionary_name': 'surnames', 'l33t': True, 'sub': {'3': 'e', '4': 'a'}, 'sub_display': '3 -> e'}))

    inp = input('Password: ')
    print(bruteforce_guesses({'token': inp}))





