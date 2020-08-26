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

def output_board(b, winner):
    width = len(b[0])
    height = len(b)
    for y in range(height):
        for x in range(width):
            print(b[y][x], end="")
            if x < width-1:
                print("|", end="")
            if y == height//2 and x == width -1:
                print("\t\tWinner is:", winner, end="")
        print()
        print("-+-+-" if y < height-1 else "")
            

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
output_board(board1, check_winner(board1))  # Should be X wins
output_board(board2, check_winner(board2))  # Should be O wins
output_board(board3, check_winner(board3))  # Should be Draw
output_board(board4, check_winner(board4))  # Should be X wins