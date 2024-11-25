#final project
from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move between 1-9: "))
            if move < 1 or move > 9:
                raise ValueError
            row, col = divmod(move - 1, 3)
            if board[row][col] not in 'OX':
                board[row][col] = 'O'
                break
            else:
                print("It's already taken!")
        except ValueError:
            print("Error! Please enter a number between 1-9.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in 'OX':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def main():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    board[1][1] = 'X'

    while True:
        display_board(board)
        if victory_for(board, 'X'):
            print("The computer wins...")
            break
        if not make_list_of_free_fields(board):
            print("It's a draw!")
            break
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You are a winner!")
            break
        draw_move(board)

main()