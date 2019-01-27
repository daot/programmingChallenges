import random

moves = ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']

win = 0

while (win < 5):
    choice = input('> ').upper()
    rand = random.choice(moves)
    if (rand == choice):
        print('It\'s a tie!')

    if (choice == 'ROCK' and rand == 'SCISSORS'):
        print('Rock crushes Scissors, you win!')
        win += 1
    if (choice == 'ROCK' and rand == 'LIZARD'):
        print('Rock crushes Lizard, you win!')
        win += 1
    if (choice == 'PAPER' and rand == 'ROCK'):
        print('Paper covers Rock, you win!')
        win += 1
    if (choice == 'PAPER' and rand == 'SPOCK'):
        print('Paper disproves Spock, you win!')
        win += 1
    if (choice == 'SCISSORS' and rand == 'PAPER'):
        print('Scissors cuts Paper, you win!')
        win += 1
    if (choice == 'SCISSORS' and rand == 'LIZARD'):
        print('Scissors decapitates Lizard, you win!')
        win += 1
    if (choice == 'LIZARD' and rand == 'PAPER'):
        print('Lizard eats Paper, you win!')
        win += 1
    if (choice == 'LIZARD' and rand == 'SPOCK'):
        print('Lizard poisons Spock, you win!')
        win += 1
    if (choice == 'SPOCK' and rand == 'ROCK'):
        print('Spock vaporizes Rock, you win!')
        win += 1
    if (choice == 'SPOCK' and rand == 'SCISSORS'):
        print('Spock smashes Scissors, you win!')
        win += 1

    if (rand == 'ROCK' and choice == 'SCISSORS'):
        print('Rock crushes Scissors, I win!')
    if (rand == 'ROCK' and choice == 'LIZARD'):
        print('Rock crushes Lizard, I win!')
    if (rand == 'PAPER' and choice == 'ROCK'):
        print('Paper covers Rock, I win!')
    if (rand == 'PAPER' and choice == 'SPOCK'):
        print('Paper disproves Spock, I win!')
    if (rand == 'SCISSORS' and choice == 'PAPER'):
        print('Scissors cuts Paper, I win!')
    if (rand == 'SCISSORS' and choice == 'LIZARD'):
        print('Scissors decapitates Lizard, I win!')
    if (rand == 'LIZARD' and choice == 'PAPER'):
        print('Lizard eats Paper, I win!')
    if (rand == 'LIZARD' and choice == 'SPOCK'):
        print('Lizard poisons Spock, I win!')
    if (rand == 'SPOCK' and choice == 'ROCK'):
        print('Spock vaporizes Rock, I win!')
    if (rand == 'SPOCK' and choice == 'SCISSORS'):
        print('Spock smashes Scissors, I win!')
