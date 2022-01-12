'''
Name: Daniel Greenwell
Class: CSE 210
Assignment: W02 Prove: Developer - Solo Code Submission
'''

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def winner_message(board):
    if board[0] == board[1] == board[2]:
        return (print(f"{board[0]} wins!"))
    elif board[3] == board[4] == board[5]:
        return (print(f"{board[3]} wins!"))
    elif board[6] == board[7] == board[8]:
        return (print(f"{board[6]} wins!"))
    elif board[0] == board[3] == board[6]:
        return (print(f"{board[0]} wins!"))
    elif board[1] == board[4] == board[7]:
        return (print(f"{board[1]} wins!"))
    elif board[2] == board[5] == board[8]:
        return (print(f"{board[2]} wins!"))
    elif board[0] == board[4] == board[8]:
        return (print(f"{board[0]} wins!"))
    elif board[2] == board[4] == board[6]:
        return (print(f"{board[2]} wins!"))

def make_move(player, board):
    square = int(input(f"{player}, please choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    winner_message(board)
    print("Good game. Thanks for playing!")
    
if __name__ == "__main__":
    main()
