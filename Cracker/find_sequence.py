''' Takes all of the matches found in mymatching.py and creates a
consecutive sequence of dictionary and bruteforce matches, sorted by
appearance in the password. '''

def search(password, matches):
    ''' See module docstring '''

    output = []
    used_entries = []
    brute = []
    brute_positions = []

    password_buffer = list(password)

    for match in matches:
        if match['i'] not in used_entries:
            if match['j'] not in used_entries:
                output.append(match)
                for character in range(match['i'], match['j'] + 1):
                    password_buffer[character] = 'OUT'
                    used_entries.append(character)


    for position, value in enumerate(password_buffer):
        if value != 'OUT':
            brute.extend(value)
            brute_positions.append(position)
        if (value == 'OUT' and brute) or (position == (len(password_buffer) - 1) and brute):
            bf_word = ('').join(brute)
            output.append({
                'pattern': 'bruteforce',
                'i': brute_positions[0],
                'j': brute_positions[-1],
                'token': bf_word,
                'matched_length': len(bf_word)
                })
            brute = []
            brute_positions = []


    return sorted(output, key=lambda x: x['i'])
