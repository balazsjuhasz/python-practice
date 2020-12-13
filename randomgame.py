import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])
number = random.randint(start, end)

while True:
    try:
        answer = int(input(f'Guess a number between {start} and {end}: '))

        if answer == number:
            print('You guessed correctly.')
            break

        print(f'Wrong answer, please try again')

    except ValueError:
        print('Please enter a valid number')
        continue
