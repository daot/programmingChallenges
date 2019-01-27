board = [['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]

player = 0

while(True):
    while(player == 0):
        count = 0
        for i in range(0, 5):
            for x in range(0, 5):
                print(board[i][x], end='')
            print()
        choice = input('X > ')
        while(choice is ''):
            choice = input('Pick again: ')
        choice = int(choice)

        for x in range(1, 6):
            if choice is x:
                place = 0
                for i in range(0, 5):
                    if board[4 - i][x - 1] is '[ ]':
                        board[4 - i][x - 1] = '[X]'
                        break
        player = 1

    while(player == 1):
        count = 0
        for i in range(0, 5):
            for x in range(0, 5):
                print(board[i][x], end='')
            print()
        choice = input('O > ')
        while(choice is ''):
            choice = input('Pick again: ')
        choice = int(choice)

        for x in range(1, 6):
            if choice is x:
                place = 0
                for i in range(0, 5):
                    if board[4 - i][x - 1] is '[ ]':
                        board[4 - i][x - 1] = '[O]'
                        break
        player = 0
