from time import time

def crack():

    found = False

    inp = input('Password: ')

    start = time()

    with open('../dicts/txt-files/passwords.txt') as f:
        for guesses, line in enumerate(f):
            if inp == line.split(' ')[0]:
                print('Password found, it took ', guesses, ' guesses')
                found = True
                break
    
    if found is False:
        print('Password not found in ', guesses, ' guesses')

    end = time()
    total_time = end - start

    print('This took', total_time, 'seconds at', guesses / total_time, 'guesses/second')



if __name__ == '__main__':
    crack()

