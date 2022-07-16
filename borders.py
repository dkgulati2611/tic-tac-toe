board = {'7' : ' ','8' : ' ','9' : ' ',
         '4' : ' ','5' : ' ','6' : ' ',
         '1' : ' ','2' : ' ','3' : ' '}
boardkeys = []
# print(boardkeys)
for key in board:
    boardkeys.append(key)
# print(boardkeys)
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# printboard(board)

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printboard(board)
        print("it's turn of " + turn +  "specify the place u want to")
        move = input()
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else : 
            print("sorry this cell location is filled choose an another option")

            continue
        if count>=5:
            if board['7'] == board['8'] == board['9'] != ' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break

            if board['4']==board['5']== board['6'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break
            if board['1']==board['2']== board['3'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break
            if board['1']==board['4']== board['7'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break
            if board['3']==board['6']== board['9'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break
            if board['1']==board['5']== board['9'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break
            if board['3']==board['5']== board['7'] !=' ':
                printboard(board)
                print("\ngame over\n")
                print("player " +turn+ "won the game")

                break

        if count==9:
            print("\ngame over\n The game is tie")

        if turn == 'X':
            turn = 'O'
        else :
            turn = 'X'

    restart = input("do u want to restart? (y/n) : ")
    if restart == 'y' or restart =='Y':
        for key in boardkeys:
            board[key] = ' '

        game()

if __name__ == "__main__":
    game()


