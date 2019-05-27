'''
Builds lists of passwords for use with the main checker
'''

import os

def list_builder():

    # Available lists are:
    #   passwords.txt
    #   english_wikipedia.txt
    #   us_tv_and_film.txt
    #   male_names.txt
    #   female_names.txt
    #   surnames.txt

    word_list = []

    dicts = [os.path.join('../dicts', x) for x in os.listdir('../dicts/') if x.endswith('.txt')]
   
    print(dicts)

    for i in dicts:
        with open(i, 'r') as f:
            word_list.extend(f.readlines())


if __name__ == '__main__':
    list_builder()


