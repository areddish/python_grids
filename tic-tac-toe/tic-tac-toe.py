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

# This outputs the board
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
    # Implement this function to determine who won, X, O, or Draw

    return "Not implemented yet"


# Test cases
output_board(board1, check_winner(board1))  # Should be X wins
output_board(board2, check_winner(board2))  # Should be O wins
output_board(board3, check_winner(board3))  # Should be Draw
output_board(board4, check_winner(board4))  # Should be X wins