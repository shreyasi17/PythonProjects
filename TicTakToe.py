TheBoard = {'Top-L': ' ' , 'Top-M': ' ' , 'Top-R': ' ' ,
            'Mid-L': ' ' , 'Mid-M': ' ' , 'Mid-R': ' ' ,
            'Low-L': ' ' , 'Low-M': ' ' , 'Low-R': ' ' }

board_keys = []

for key in TheBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['Top-L'] + '|' + board['Top-M'] + '|' + board['Top-R'])
    print('-+-+-')
    print(board['Mid-L'] + '|' + board['Mid-M'] + '|' + board['Mid-R'])
    print('-+-+-')
    print(board['Low-L'] + '|' + board['Low-M'] + '|' + board['Low-R'])

def Game():

    turn = 'X'
    count = 0
    flag = 0

    print('Top-L | Top-M | Top-R')
    print('------+-------+------')
    print('Mid-L | Mid-M | Mid-R')
    print('------+-------+------')
    print('Low-L | Low-M | Low-R')
    print('\n \n ')


    for i in range(10):
        printBoard(TheBoard)
        print('\n \n Its your turn ' + turn + '. Enter your position as mentioned above.')

        move = input()

        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count += 1

        else:
            print('This place is already filled.')
            continue

        if count >= 5:

            if TheBoard['Top-L'] == TheBoard['Top-M'] == TheBoard['Top-R']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Mid-L'] == TheBoard['Mid-M'] == TheBoard['Mid-R']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Low-L'] == TheBoard['Low-M'] == TheBoard['Low-R']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Top-L'] == TheBoard['Mid-L'] == TheBoard['Low-L']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Top-M'] == TheBoard['Mid-M'] == TheBoard['low-M']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Top-R'] == TheBoard['Mid-R'] == TheBoard['Low-R']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Top-L'] == TheBoard['Mid-M'] == TheBoard['Low-R']:
                printBoard(TheBoard)
                flag = 1
                break

            elif TheBoard['Top-R'] == TheBoard['Mid-M'] == TheBoard['Low-L']:
                printBoard(TheBoard)
                flag = 1
                break

        if count == 9:
            print('\n \n ***** GAME OVER *****')
            print('''**** It's a tie ****''')
        
        if turn == 'X':
            turn = 'O'

        else:
            turn = 'X'

    if flag == 1:
            print('\n \n ***** GAME OVER *****')
            print('***** ' + turn + ' OWN *****')
            

    restart = input("Do want to play Again?(Y / N)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            TheBoard[key] = " "

        Game()

if __name__ == "__main__":
    Game()

          
            
