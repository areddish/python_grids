# maze iter

# Helper function to load the grid
def load_grid(filename):
    grid = []
    with open(filename) as file:
        for l in file.readlines():
            grid.append(list(l.strip()))

    return grid

# Helper function to print out the grid
def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            print(grid[y][x],end="")
        print()

# Helper function to find the location of a specific character
def find(grid, ch):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == ch:
                return (x,y)

    return None

# Find a solution.
# Two options, return true/false if you find a solution
# Extra credit: return the path you found in the maze so that
#               you can display the path.
def solve(grid, start, end):
    visited = []       
    reachable = [start]
    path = [start]
    while reachable:
        cur = reachable.pop()
        path.append(cur)
        if cur == end:           
            return path

        visited.append(cur)
        for move in [(-1,0), (1,0), (0,-1), (0,1)]:
            after_move = (cur[0]+move[0], cur[1]+move[1])
            if after_move in visited or grid[after_move[1]][after_move[0]] == "#":
                continue

            reachable.append(after_move)

    return None

if __name__ == "__main__":
    # Allow for maze's to be passed in on the command line:
    # python maze.py maze.txt
    import sys
    maze = sys.argv[1] if len(sys.argv) > 1 else "maze.txt"

    # Load the grid
    grid = load_grid(maze)

    # compute a solution
    start = find(grid, "S")
    end = find(grid, "E")
    solution = solve(grid, start, end)

    if solution:
        print ("Found solution!")
        import time
        import os
        prev = start
        for x in solution[:-1]:
            os.system('cls')
            grid[x[1]][x[0]] = "*"
            grid[prev[1]][prev[0]] = "."
            prev = x
            print_grid(grid)
            time.sleep(0.12)
    else: 
        print ("No solution!")

    # Extra credit: print out the maze with your solution    