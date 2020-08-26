grid = []
with open("spreadsheet_formula_dependency.txt") as file:
    for l in file.readlines():
        grid.append(l.strip().split(","))

def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            print("{:11s}".format(grid[y][x]),end="")
        print()

def column_window(grid, column, start, stop):
    result = []
    for y in range(start,stop):
        result.append(float(eval(grid, column, y)))
    return result

# Formula implementations
def mul(grid, x, y):
    return str(float(eval(grid, x-2, y)) * float(eval(grid, x-1, y)))

def add(grid, x, y):
    return str(sum(column_window(grid, x, 1, y)))

def eval(grid, x, y):
    formulas = {
        "*": mul,
        "+": add
    }

    op = grid[y][x]
    if op in formulas:
        return formulas[op](grid, x, y)

    return op

# Iterate over grid and fill in formulas
def fill_in_formulas(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            grid[y][x] = eval(grid, x, y)

print_grid(grid)
fill_in_formulas(grid)
print_grid(grid)