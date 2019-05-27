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

    return sorted(matches, key=lambda x: x['matched_length'], reverse=True)


# dictionary match (common passwords, english, last names, etc)
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


def relevant_l33t_subtable(password, table):
    password_chars = {}
    for char in list(password):
        password_chars[char] = True

    subtable = {}
    for letter, subs in table.items():
        relevant_subs = [sub for sub in subs if sub in password_chars]
        if len(relevant_subs) > 0:
            subtable[letter] = relevant_subs

    return subtable


def enumerate_l33t_subs(table):
    keys = list(table.keys())
    subs = [[]]

    def dedup(subs):
        deduped = []
        members = {}
        for sub in subs:
            assoc = [(k, v) for v, k in sub]
            assoc.sort()
            label = '-'.join([k + ',' + str(v) for k, v in assoc])
            if label not in members:
                members[label] = True
                deduped.append(sub)

        return deduped

    def helper(keys, subs):
        if not len(keys):
            return subs

        first_key = keys[0]
        rest_keys = keys[1:]
        next_subs = []
        for l33t_chr in table[first_key]:
            for sub in subs:
                dup_l33t_index = -1
                for i in range(len(sub)):
                    if sub[i][0] == l33t_chr:
                        dup_l33t_index = i
                        break
                if dup_l33t_index == -1:
                    sub_extension = list(sub)
                    sub_extension.append([l33t_chr, first_key])
                    next_subs.append(sub_extension)
                else:
                    sub_alternative = list(sub)
                    sub_alternative.pop(dup_l33t_index)
                    sub_alternative.append([l33t_chr, first_key])
                    next_subs.append(sub)
                    next_subs.append(sub_alternative)

        subs = dedup(next_subs)
        return helper(rest_keys, subs)

    subs = helper(keys, subs)
    sub_dicts = []  # convert from assoc lists to dicts
    for sub in subs:
        sub_dict = {}
        for l33t_chr, chr in sub:
            sub_dict[l33t_chr] = chr
        sub_dicts.append(sub_dict)

    return sub_dicts


def translate(string, chr_map):
    chars = []
    for char in list(string):
        if chr_map.get(char, False):
            chars.append(chr_map[char])
        else:
            chars.append(char)

    return ''.join(chars)


def l33t_match(password, _ranked_dictionaries=RANKED_DICTIONARIES,
               _l33t_table=L33T_TABLE):
    matches = []

    for sub in enumerate_l33t_subs(
            relevant_l33t_subtable(password, _l33t_table)):
        if not len(sub):
            break

        subbed_password = translate(password, sub)
        for match in dictionary_match(subbed_password, _ranked_dictionaries):
            token = password[match['i']:match['j'] + 1]
            if token.lower() == match['matched_word']:
                # only return the matches that contain an actual substitution
                continue

            # subset of mappings in sub that are in use for this match
            match_sub = {}
            for subbed_chr, chr in sub.items():
                if subbed_chr in token:
                    match_sub[subbed_chr] = chr
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
