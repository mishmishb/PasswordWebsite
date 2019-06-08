''' Takes all of the found_words found in word_extraction.py and creates a
consecutive sequence of dictionary and bruteforce sequences, sorted by
appearance in the password. '''

def make_sequence(password, found_words):
    ''' See module docstring '''

    output = []
    used_entries = []
    brute = []
    brute_positions = []

    # Creates a buffer so that this can have characters swapped out
    # to indicate they have already been used
    password_buffer = list(password)

    # For each word that has been found, append the first word
    # to the output. This works because the words have been pre
    # sorted by word_extraction.py by length, whether they have
    # l33t characters, and their rank
    for word in found_words:
        if word['i'] not in used_entries:
            if word['j'] not in used_entries:
                output.append(word)
                for character in range(word['i'], word['j'] + 1):
                    # Once the space has been taken up, mark it as
                    # so, allowing the unused space to be treated
                    # as needing brute-force calculations
                    password_buffer[character] = 'OUT'
                    used_entries.append(character)


    position_help = len(password_buffer) - 1
    # Store details of sequences that must be brute-forced
    for position, value in enumerate(password_buffer):
        if value != 'OUT':
            # If the character is not part of a word, add
            # the character and its position to the relevant
            brute.extend(value)
            brute_positions.append(position)
        # If the current character is either part of a word, or is the final
        # character in the password, and the previous characters have been
        # non-word characters, then add everything up to that point to
        # the output as a brute-force segment
        if (value == 'OUT' and brute) or (position == position_help and brute):
            bf_word = ('').join(brute)
            output.append({
                'i': brute_positions[0],
                'j': brute_positions[-1],
                'pattern_type': 'bruteforce',
                'input': bf_word,
                'length': len(bf_word)
                })
            brute = []
            brute_positions = []


    return sorted(output, key=lambda x: x['i'])
