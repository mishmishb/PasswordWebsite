
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


def dictionary_guess(match, dictionary_length=10000):

    guesses = match['rank'] + (dictionary_length * uppercase_character_guesses(match) \
                                                 * l33t_character_guesses(match))

    return guesses


def uppercase_character_guesses(match):

    word = match['token']

    if word.islower():
        return 0

    uppercase_count = 0
    lowercase_count = 0

    for letter in list(word):
        if letter.isupper():
            uppercase_count += 1

    if (word[0].isupper() and uppercase_count == 1):
        return 1
    
    if ((word[-1].isupper() and uppercase_count == 1) or word.isupper()):
        return 2.5

    dictionary_loops = 0
    for k in range(1, uppercase_count + 1):
        if k == uppercase_count:
            dictionary_loops += (nCk(len(word), k) / 2)
        else:
            dictionary_loops += nCk(len(word), k)

    return dictionary_loops


def l33t_character_guesses(match):
    if not match.get('l33t', False):
        return 1

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


    print(l33t_character_guesses({'pattern': 'bruteforce', 'i': 0, 'j': 2, 'token': 'zkr', 'matched_length': 3}, {'pattern': 'dictionary', 'i': 3, 'j': 7, 'token': 'L3mon', 'matched_word': 'lemon', 'matched_length': 5, 'rank': 1686, 'dictionary_name': 'surnames', 'l33t': True, 'sub': {'3': 'e'}, 'sub_display': '3 -> e'}, {'pattern': 'bruteforce', 'i': 8, 'j': 10, 'token': '%57', 'matched_length': 3}, {'pattern': 'dictionary', 'i': 11, 'j': 18, 'token': 'passwOrd', 'matched_word': 'password', 'matched_length': 8, 'rank': 2, 'dictionary_name': 'passwords', 'l33t': False}))







