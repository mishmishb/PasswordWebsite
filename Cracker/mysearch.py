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


if __name__ == '__main__':

	start = time()

	password = 'tyqewxt3stingzfhHelpwtg'
	
	matches = [{'pattern': 'dictionary', 'i': 6, 'j': 12, 'token': 't3sting', 'matched_word': 'testing', 'matched_length': 7, 'rank': 398, 'dictionary_name': 'passwords', 'l33t': True, 'sub': {'3': 'e'}, 'sub_display': '3 -> e'}, {'pattern': 'dictionary', 'i': 6, 'j': 11, 'token': 't3stin', 'matched_word': 'testin', 'matched_length': 6, 'rank': 22215, 'dictionary_name': 'passwords', 'l33t': True, 'sub': {'3': 'e'}, 'sub_display': '3 -> e'}, {'pattern': 'dictionary', 'i': 8, 'j': 12, 'token': 'sting', 'matched_word': 'sting', 'matched_length': 5, 'rank': 2801, 'dictionary_name': 'passwords', 'l33t': False}, {'pattern': 'dictionary', 'i': 9, 'j': 12, 'token': 'ting', 'matched_word': 'ting', 'matched_length': 4, 'rank': 3313, 'dictionary_name': 'passwords', 'l33t': False}, {'pattern': 'dictionary', 'i': 16, 'j': 19, 'token': 'Help', 'matched_word': 'help', 'matched_length': 4, 'rank': 103, 'dictionary_name': 'us_tv_and_film', 'l33t': False}, {'pattern': 'dictionary', 'i': 6, 'j': 9, 'token': 't3st', 'matched_word': 'test', 'matched_length': 4, 'rank': 93, 'dictionary_name': 'passwords', 'l33t': True, 'sub': {'3': 'e'}, 'sub_display': '3 -> e'}, {'pattern': 'dictionary', 'i': 10, 'j': 11, 'token': 'in', 'matched_word': 'in', 'matched_length': 2, 'rank': 4, 'dictionary_name': 'english_wikipedia', 'l33t': False}, {'pattern': 'dictionary', 'i': 16, 'j': 17, 'token': 'He', 'matched_word': 'he', 'matched_length': 2, 'rank': 12, 'dictionary_name': 'english_wikipedia', 'l33t': False}, {'pattern': 'dictionary', 'i': 10, 'j': 10, 'token': 'i', 'matched_word': 'i', 'matched_length': 1, 'rank': 2, 'dictionary_name': 'us_tv_and_film', 'l33t': False}]

	print(search(password, matches))

	end = time()

	print(end - start, 'seconds')


'''
pass: testGYHripple356demonstrate
demonstrate
ripple
test
'''