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
            

def find_winner(board, x, y, winning_length=3):
    # Start with a count of 0, check all of the diagnoals
    match_count = 0

    # Diagonal Down [0][0], [1][1], [2][2] as a 3x3 example
    for j in range(winning_length):
        if board[j][j] == board[y][x]:
            match_count += 1

    if match_count == winning_length:
        return board[y][x]

    # Diagonal Up [2][0], [1][1], [0][2] as a 3x3 example
    match_count = 0
    for j in range(winning_length):
        if board[winning_length - 1 - j][j] == board[y][x]:
            match_count += 1

    if match_count == winning_length:
        return board[y][x]

    # Horizontal

    # From now one we start at a count of 1, since the piece that was just played
    # is already counted, just look around.
    match_count = 1
    current_x = x
    while (current_x > 0 and board[y][current_x-1] == board[y][x]):
        match_count += 1
        current_x -= 1

    current_x = x
    while (current_x < len(board[0])-1 and board[y][current_x+1] == board[y][x]):
        match_count += 1
        current_x += 1

    if match_count == winning_length:
        return board[y][x]

    # Vertical
    match_count = 1
    current_y = y
    while (current_y > 0 and board[current_y-1][x] == board[y][x]):
        match_count += 1
        current_y -= 1

    current_y = y
    while (current_y < len(board)-1 and board[current_y+1][x] == board[y][x]):
        match_count += 1
        current_y += 1

    if match_count == winning_length:
        return board[y][x]

    return "Draw"


# Test cases
print("board1 winner is", find_winner(board1, 2, 2), "It should be", "X")
print("board2 winner is", find_winner(board2, 0, 2), "It should be", "O")
print("board3 winner is", find_winner(board3, 1, 1), "It should be", "Draw")
print("board4 winner is", find_winner(board4, 2, 1), "It should be", "X")


