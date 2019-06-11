''' Module for providing useful advice to the users based on the
password that is tested. Aims to assist with pushing people
towards better password habits. '''


def advice_generator(password, sequence):
    ''' Master function that combines the different types
    of advice together. '''

    advice_dict = {}

    general_advice(password, sequence, advice_dict)
    set_size_advice(password, advice_dict)
    bruteforce_advice(sequence, advice_dict)
    dictionary_advice(sequence, advice_dict)

    return advice_dict


def general_advice(password, sequence, advice_dict):
    ''' Provides some general advice on the password as a whole,
    such as increasing the length, and avoiding dictionary words. '''


    advice_list = []

    # Even with a full set of randomly selected characters,
    # 6 characters or less is too easy to crack in many cases.
    length = len(password)
    if length < 7:
        advice_list.append('This password is definitely too short!')
    # Research by Shen et al. (2016) showed that the mean length
    # of a password is 9.46 characters.
    elif length < 11:
        advice_list.append(
            'Most passwords are around this length '
            'but you can definitely do better!'
            )
    else:
        advice_list.append('This password is a good length')

    for section in sequence:
        # Passwords based on dictionary words are rarely as secure
        # as people think. To be secure it needs to be long enough
        # that it would be better off using a mnemonic device.
        if section.get('word_list'):
            advice_list.append(
                'This password contains dictionary words '
                'and these are rarely that secure, have you '
                'tried using a mnemonic device?'
                )
            break

    advice_dict['General: '] = advice_list

    return advice_dict


def set_size_advice(password, advice_dict):
    ''' Looks at the password as a whole and calculates which sets
    of characters are used. '''

    advice_list = []
    set_list = []
    low_alpha = False
    upper_alpha = False
    number = False
    symbol = False
    potential_symbols = r'!"£$€%^&*()-_=;:+[]{}#~\'@/?.>,<|`¬'

    # Borrowed from calculate_guesses.bruteforce_guesses()
    for character in password:
        if (character.islower() and low_alpha is False):
            low_alpha = True
        elif (character.isupper() and upper_alpha is False):
            upper_alpha = True
        elif (character.isdecimal() and number is False):
            number = True
        elif(character in potential_symbols and symbol is False):
            symbol = True
        if False not in (low_alpha, upper_alpha, number, symbol):
            break

    # Evaluates the character sets used to provide feedback of what
    # is missing
    if False in (low_alpha, upper_alpha, number, symbol):
        set_list.append('This password doesn\'t contain')
        if low_alpha is False:
            set_list.append(' lowercase letters,')
        if upper_alpha is False:
            set_list.append(' capital letters,')
        if number is False:
            set_list.append(' numbers,')
        if symbol is False:
            set_list.append(' symbols.')
        advice_list.append(('').join(set_list)[:-1] + '.')
    else:
        advice_list.append(
            'This password contains a full set of characters, great!'
        )

    advice_dict['Set size: '] = advice_list

    return advice_dict


def bruteforce_advice(sequence, advice_dict):
    ''' Checks which character sets are used in the brute-force
    sections of the password (if they exist) and suggests
    increasing the set size if the full set isn't used. '''

    low_alpha = False
    upper_alpha = False
    number = False
    symbol = False

    for section in sequence:
        if not section.get('word_list'):
            # Checks which character sets are in the sequence.
            if 'lowercase' in section['character_space']:
                low_alpha = True
            if 'uppercase' in section['character_space']:
                upper_alpha = True
            if 'number' in section['character_space']:
                number = True
            if 'symbol' in section['character_space']:
                symbol = True
    if False in (low_alpha, upper_alpha, number, symbol):
        advice_dict['Brute-force: '] = [
            'The brute-force sections of the password '
            'don\'t contain a full character set, maybe '
            'expand this.'
            ]

    # If there are no brute-force sections
    if True not in (low_alpha, upper_alpha, number, symbol):
        advice_dict['Brute-force: '] = [
            'This password is entirely comprised of '
            'dictionary words'
            ]

    return advice_dict


def dictionary_advice(sequence, advice_dict):
    ''' Advice generator for dictionary words, checks for
    common words, and names which are likely to be personally
    meaningful. '''

    for section in sequence:
        advice_list = []
        if section.get('word_list'):
            # Ideally words would be avoided, but ESPECIALLY
            # commonly used words should always be avoided.
            if section['word_list'] in (
                    'passwords', 'english_wikipedia', 'us_tv_and_film'
            ):
                if section['rank'] <= 10:
                    advice_list.append(
                        f"{section['found_word']} "
                        "is a top 10 most common word in "
                        f"{section['word_list']}"
                        )
                elif section['rank'] <= 100:
                    advice_list.append(
                        f"{section['found_word']} "
                        "is a top 100 most common word in "
                        f"{section['word_list']}"
                        )
                elif section['rank'] <= 1000:
                    advice_list.append(
                        f"{section['found_word']} "
                        "is a top 1000 most common word in "
                        f"{section['word_list']}"
                        )
                elif section['rank'] <= 10000:
                    advice_list.append(
                        f"{section['found_word']} "
                        "is a top 10000 most common word in "
                        f"{section['word_list']}"
                        )
            # Names in particular are a bad idea as they are
            # often chosen due to being particularly meaningful.
            # Putting the person in danger of social engineering.
            elif section['word_list'] in (
                    'male_names', 'female_names', 'surnames'
            ):
                advice_list.append(
                    'If this name is personally meaningful to you '
                    'it is HIGHLY RECOMMENDED you avoid using it'
                    )
            if section.get('uppercase_style'):
                if section['uppercase_style'] == 'First or ALL':
                    advice_list.append(
                        'This type of uppercasing is very obvious. '
                        r'Over 80% of uppercased words are either '
                        'First letter uppercased or ALL uppercased.'
                        )
        if advice_list:
            advice_dict[section['input'] + ': '] = advice_list


    return advice_dict
