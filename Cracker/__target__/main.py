from time import time

import mymatching, mysearch, guesses, guesses_to_time

def mystrengthtool(password):

    
    
    ranked_dictionaries = mymatching.produce_ranked_dict()
    matches = mymatching.omnimatch(password, ranked_dictionaries)
    #sequence = mysearch.search(password, matches)
    #no_of_guesses = guesses.guess_calculator(sequence)
    #ctime = guesses_to_time.calc_time(no_of_guesses)
    #return [no_of_guesses, sequence, ctime]
    console.log(matches.pattern, matches.token, matches.rank)
    return matches
    

def main_checker():
    
    user_password = document.getElementById('my_input').value
    results = mystrengthtool(user_password)
    document.getElementById('final_output').innerHTML = results
    
