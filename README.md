# Code With Me Meetup on Grids using Python

## Problem #1

### [Tic-Tac-Toe](https://github.com/areddish/python_grids/tree/master/tic-tac-toe)

Given a Tic-Tac-Toe board, determine who won:

- X
- O
- Draw!

```Python
board1 = [ ["X", "O", "X"],
           ["O", "X", "O"],
           ["O", "X", "X"] ]
```

## Problem #2

### [Spreadsheets](https://github.com/areddish/python_grids/tree/master/spreadsheet)

Given a spreadsheet, fill in the formula:

- \* means fill this cell with the multiplication of the previous two cells in this row
- \+ means fill this cell with the sum of the columns of values that occur above this cell.

```Text
Phone      Part #     Qty        Price      Profit
555-1000   33AA56     3          25         *
555-4033   11AB11     5          30         *
555-1406   24CB13     100        1.25       *
555-4445   24CB15     2000       1          *
                      +                     +
```

## Problem #3

### [Maze](https://github.com/areddish/python_grids/tree/master/maze)

Given a maze, determine if you can move from start (_S_) to end (_E_) navigating around the walls (_#_)

```Text
#######################
#S#   #   #     #   # #
# # # # # # ##### # # #
# # # # #         #   #
# # # # # ### # # #####
#   #   #     # #    E#
#######################
```

_Extra Credit: return the path!_
