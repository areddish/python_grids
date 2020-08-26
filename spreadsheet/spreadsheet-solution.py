grid = []
with open("spreadsheet_formula.txt") as file:
    for l in file.readlines():
        grid.append(l.strip().split(","))

def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            print("{:11s}".format(grid[y][x]),end="")
        print()

def column_window(grid, column, start,stop):
    result = []
    for row in grid[start:stop]:
        result.append(float(row[column]))
    return result

# Formula implementations
def mul(grid, x, y):
    return str(float(grid[y][x-2]) * float(grid[y][x-1]))
def add(grid, x, y):
    return str(sum(column_window(grid, x, 1, y)))

# Iterate over grid and fill in formulas
def fill_in_formulas(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "*":
                grid[y][x] = mul(grid, x, y)
            elif grid[y][x] == "+":
                grid[y][x] = add(grid, x, y)

print_grid(grid)
fill_in_formulas(grid)
print_grid(grid)