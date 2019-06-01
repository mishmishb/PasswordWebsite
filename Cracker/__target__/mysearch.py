from time import time

def search(password, matches):

	output = []
	used_entries = []
	bruteforce_strings = []
	brute = []
	brute_positions = []

	password_buffer = list(password)

	for match in matches:
		if (match['i'] or match['j']) not in used_entries:
			output.append(match)
			for x in range(match['i'], match['j'] + 1):
				password_buffer[x] = 'OUT'
				used_entries.append(x)


	for position, value in enumerate(password_buffer):
		if value is not 'OUT':
			brute.extend(value)
			brute_positions.append(position)
		if (value is 'OUT' and brute) or (position == (len(password_buffer) - 1) and brute):
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


	return sorted(output, key=lambda x: (x['i'], x['j']))

