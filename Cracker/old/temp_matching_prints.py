from frequency_lists import FREQUENCY_LISTS
from time import time


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
        l33t_match,
    ]:
        matches.extend(matcher(password, _ranked_dictionaries=_ranked_dictionaries))

    return sorted(matches, key=lambda x: (x['i'], x['j']))


# dictionary match (common passwords, english, last names, etc)
def dictionary_match(password, _ranked_dictionaries=RANKED_DICTIONARIES):
    print("1 Performing Dictionary Match")
    matches = []
    length = len(password)
    print("2 Password length is:\t", length)
    password_lower = password.lower()
    for dictionary_name, ranked_dict in _ranked_dictionaries.items():
        # print("Word:\t", dictionary_name, ":", ranked_dict)
        for i in range(length):
            for j in range(i, length):
                print("3 Word:\t", password_lower[i:j+1], "\tin\t", dictionary_name)
                if password_lower[i:j + 1] in ranked_dict:
                    print("4", password_lower[i:j+1], "\tis a match in\t", dictionary_name)
                    word = password_lower[i:j + 1]
                    rank = ranked_dict[word]    
                    matches.append({
                        'pattern': 'dictionary',
                        'i': i,
                        'j': j,
                        'token': password[i:j + 1],
                        'matched_word': word,
                        'rank': rank,
                        'dictionary_name': dictionary_name,
                        'reversed': False,
                        'l33t': False,
                    })

    return sorted(matches, key=lambda x: (x['i'], x['j']))


def relevant_l33t_subtable(password, table):
    print("5 Looking up relevant l33t subtable")
    password_chars = {}
    for char in list(password):
        password_chars[char] = True
    print("6", password_chars)

    subtable = {}
    for letter, subs in table.items():
        relevant_subs = [sub for sub in subs if sub in password_chars]
        if len(relevant_subs) > 0:
            print("7", relevant_subs)
            subtable[letter] = relevant_subs
    print("8", subtable)

    return subtable


def enumerate_l33t_subs(table):
    print("9 Enumerating l33t subs")
    keys = list(table.keys())
    print("10", keys)
    subs = [[]]

    def dedup(subs):
        print("11 Deduping")
        deduped = []
        members = {}
        for sub in subs:
            assoc = [(k, v) for v, k in sub]
            assoc.sort()
            print("12", assoc)
            label = '-'.join([k + ',' + str(v) for k, v in assoc])
            if label not in members:
                members[label] = True
                deduped.append(sub)
        print("13 Subs:\t", subs)      
        print("14 Deduped:\t", deduped)

        return deduped

    def helper(keys, subs):
        print("15 l33t sub helper")
        if not len(keys):
            return subs

        first_key = keys[0]
        rest_keys = keys[1:]
        next_subs = []
        for l33t_chr in table[first_key]:
            print("16 l33t character:\t", l33t_chr)
            for sub in subs:
                print("17 sub:\t", sub)
                dup_l33t_index = -1
                for i in range(len(sub)):
                    print("18 sub[i]:\t", sub[i])
                    if sub[i][0] == l33t_chr:
                        dup_l33t_index = i
                        break
                if dup_l33t_index == -1:
                    print("19 dup_l33t_index is -1")
                    sub_extension = list(sub)
                    print("20 sub extension:\t", sub_extension)
                    sub_extension.append([l33t_chr, first_key])
                    print("21 sub extension:\t", sub_extension)
                    next_subs.append(sub_extension)
                    print("22 next subs:\t", next_subs)
                else:
                    print("23 dup_l33t_index is not -1")
                    sub_alternative = list(sub)
                    print("24 sub alternative:\t", sub_alternative)
                    sub_alternative.pop(dup_l33t_index)
                    print("25 Popped dup_l33t_index from sub_alternative")
                    sub_alternative.append([l33t_chr, first_key])
                    next_subs.append(sub)
                    next_subs.append(sub_alternative)

        subs = dedup(next_subs)
        print("26 Loop finished, subs:\t", subs)
        return helper(rest_keys, subs)

    subs = helper(keys, subs)
    sub_dicts = []  # convert from assoc lists to dicts
    print("27 Converting subs from lists to dicts")
    for sub in subs:
        sub_dict = {}
        for l33t_chr, chr in sub:
            sub_dict[l33t_chr] = chr
        sub_dicts.append(sub_dict)
    print("28 Final sub_dicts:\t", sub_dicts)
    return sub_dicts


def translate(string, chr_map):
    print("29 Translating:\t", string, "+", chr_map)
    chars = []
    for char in list(string):
        if chr_map.get(char, False):
            chars.append(chr_map[char])
        else:
            chars.append(char)

    print("30 Returning:\t", ''.join(chars))
    return ''.join(chars)


def l33t_match(password, _ranked_dictionaries=RANKED_DICTIONARIES,
               _l33t_table=L33T_TABLE):
    matches = []
    print("31 Performing l33t match")
    print("32 Generating relevant l33t")
    for sub in enumerate_l33t_subs(
            relevant_l33t_subtable(password, _l33t_table)):
        if not len(sub):
            break

        print("33 Translating password")
        subbed_password = translate(password, sub)
        print("34 Looping through results of using subbed passwords in dictionary match")
        print("35 Only returns matches that contain an actual substitution")
        for match in dictionary_match(subbed_password, _ranked_dictionaries):
            token = password[match['i']:match['j'] + 1]
            print("36 Token:\t", token)
            if token.lower() == match['matched_word']:
                # only return the matches that contain an actual substitution
                continue

            # subset of mappings in sub that are in use for this match
            match_sub = {}
            for subbed_chr, chr in sub.items():
                print("37 sub.items():\t", sub.items())
                if subbed_chr in token:
                    match_sub[subbed_chr] = chr
                    print("38 Subbed_chr is in token:\t", match_sub[subbed_chr])
            match['l33t'] = True
            match['token'] = token
            match['sub'] = match_sub
            match['sub_display'] = ', '.join(
                ["%s -> %s" % (k, v) for k, v in match_sub.items()]
            )
            print("39 Match:\t", match)
            matches.append(match)

    matches = [match for match in matches if len(match['token']) > 1]
    print("40 Final Matches:\t", sorted(matches, key=lambda x: (x['i'], x['j'])))

    return sorted(matches, key=lambda x: (x['i'], x['j']))


if __name__ == '__main__':

    inp = input('Password: ')

    start = time()
    
    print(omnimatch(inp, produce_ranked_dict()))
    
    end = time()

    print(end - start, 'seconds')
