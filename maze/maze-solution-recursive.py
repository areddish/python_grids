def find(grid, ch):
    width = len(grid[0])
    height = len(grid)
    print(width,height)
    for y in range(height):
        for x in range(width):
            print(x,y)
            if grid[y][x] == ch:
                return (x,y)

    return None

def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            print(grid[y][x],end="")
        print()

def get_at(grid, x, y):
    width = len(grid[0])
    height = len(grid)
    if x < 0 or x >= width or y < 0 or y >= height:
        return None

    return grid[y][x]

def load_grid(filename):
    grid = []
    with open(filename) as file:
        for l in file.readlines():
            grid.append(list(l.strip()))

    return grid

# find Ending!
def solve(grid, start, end, path=[]):
    cur = start
    # try to move in +
    moves = [ (-1, 0), (1,0), (0,-1), (0,1)]
    for move in moves:
        nx = cur[0] + move[0]
        ny = cur[1] + move[1]
        new_move = (nx,ny)

        # Don't walk back down the path we came, we've already explored it.
        if new_move in path:
            continue

        # If we hit a wall, can't go this way
        if get_at(grid,nx,ny) == "#":
            continue

        # We're going, see if we've reached the end.
        path.append(new_move)
        if get_at(grid,nx,ny) == "E":
            return path

        # nope! continue
        solution = solve(grid, new_move, end, path.copy())
        if solution:
            return solution

    return []
    

if __name__ == "__main__":
    import sys
    print(sys.argv)
    maze = sys.argv[1] if len(sys.argv) > 1 else "maze.txt"
    grid = load_grid(maze)

    start = find(grid, "S")
    end = find(grid, "E")

    solution = solve(grid,start, end)
    print(solution)

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