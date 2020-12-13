import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

while True:
    answer = int(input(f'Guess a number between {start} and {end}: '))
    number = random.randint(start, end)
    if answer == number:
        print('You guessed correctly.')
        break

    print(f'Random number was: {number}, please try again')
