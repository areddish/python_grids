# Read in the data
grid = []
with open("spreadsheet_formula.txt") as file:
    for l in file.readlines():
        grid.append(l.strip().split(","))

# Helper function to print out the grid
def print_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for y in range(height):
        for x in range(width):
            # Use fixed width formating to make things more spreadsheet like
            print("{:11s}".format(str(grid[y][x])),end="")
        print()

#
# Solution goes here :)
# 
# Write code to scan and find the formulas and replace them with the 
# correct values.
# A '*' in a cell means you should replace it's value with the multiplicate of the two cells before it in the row.
# A '+' in a cell means you should replace it's value with the sum of all of the values above it.

# Print out the grid so we see the answer
print_grid(grid)
