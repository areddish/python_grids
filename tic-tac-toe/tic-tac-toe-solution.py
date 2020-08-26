# X wins this game, diagonal
board1 = [ ["X", "O", "X"],
           ["O", "X", "O"],
           ["O", "X", "X"] ]

# O wins this game, vertical
board2 = [ ["O", "X", "O"],
           ["O", "X", "X"],
           ["O", " ", " "] ]

# Draw!
board3 = [ ["O", "X", "O"],
           ["X", "O", "O"],
           ["X", "O", "X"] ]

# X wins horizontal!
board4 = [ ["O", "X", "O"],
           ["X", "X", "X"],
           ["O", "O", " "] ]

def output_board(b):
    for y in range(3):
        for x in range(3):
            print(b[y][x], end="")
            if x < 2:
                print("|", end="")
        print()
        print("-+-+-" if y < 2 else "")
            

def check_winner(board):
    # Horizontal
    if (board[0][0] == board[0][1] == board[0][2]):
        return board[0][0]
    if (board[1][0] == board[1][1] == board[1][2]):
        return board[1][0]
    if (board[2][0] == board[2][1] == board[2][2]):
        return board[2][0]

    # Vertical
    if (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
    if (board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]
    if (board[0][2] == board[1][2] == board[2][2]):
        return board[0][2]
        
    # Diagonal
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
        return board[1][1]
 
    return "Draw!"


# Test cases
print("board1 winner is", check_winner(board1), "It should be", "X")
print("board2 winner is", check_winner(board2), "It should be", "O")
print("board3 winner is", check_winner(board3), "It should be", "Draw")
print("board4 winner is", check_winner(board4), "It should be", "X")