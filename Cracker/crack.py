from time import time

def crack():

    guesses = 0
    found = False

    inp = input('Password: ')

    start = time()

    with open('lists/10-million-password-list-top-1000000.txt') as f:
        for line in f:
            guesses += 1
            if inp == line.strip():
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

