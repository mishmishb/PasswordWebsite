
def advice_generator(password, sequence):

    advice_dict = {}
    contains_words = False

    advice_list = []
    if len(password) < 7:
        advice_list.append('This password is definitely too short!')

    for section in sequence:
        if section.get('word_list'):
            advice_list.append('This password contains dictionary words ' \
                               'and these are rarely that secure, have you ' \
                               'tried using a mnemonic device?')
            break

    if advice_list:
        advice_dict['General: '] = advice_list
    

    for section in sequence:
        if not section.get('word_list'):
            if len(section['character_space']) in (1, 2, 3):
                advice_dict['Brute-force: '] = 'The brute-force sections of the password' \
                                            'don\'t contain a full character set, maybe ' \
                                            'expand this.'
            if len(section['character_space']) == 0:
                advice_dict['Brute-force: '] = 'This password contains no bruteforce sequences!'

    

    for section in sequence:
        advice_list = []
        if section.get('word_list'):
            contains_words = True
            if section['word_list'] in ('passwords', 'english_wikipedia', 'us_tv_and_film'):
                if section['rank'] <= 10:
                    advice_list.append(f"{section['found_word']} " \
                                          'is a top 10 most common word in ' \
                                        f"{section['word_list']}")
                elif section['rank'] <= 100:
                    advice_list.append(f"{section['found_word']} " \
                                          'is a top 100 most common word in ' \
                                        f"{section['word_list']}")
                elif section['rank'] <= 1000:
                    advice_list.append(f"{section['found_word']} " \
                                    'is a top 1000 most common word in ' \
                                        f"{section['word_list']}")
                elif section['rank'] <= 10000:
                    advice_list.append(f"{section['found_word']} " \
                                         'is a top 10000 most common word in ' \
                                       f"{section['word_list']}")
            elif section['word_list'] in ('male_names', 'female_names', 'surnames'):
                advice_list.append('If this name is personally meaningful to you ' \
                                   'it is HIGHLY RECOMMENDED you avoid using it')
            if section.get('uppercase_style'):
                if section['uppercase_style'] == 'First or ALL':
                    advice_list.append('This type of uppercasing is very obvious. ' \
                                       r'Over 80% of uppercased words are either ' \
                                        'First letter uppercased or ALL uppercased.')
        if advice_list:
            advice_dict[section['input'] + ': '] = advice_list

    
    return advice_dict
        