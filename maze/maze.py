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
def solve(grid, start, end,): # Add your parameters as needed    
    # Compute any path from start to end
    return True

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
    else: 
        print ("No solution!")

    # Extra credit: print out the maze with your solution    