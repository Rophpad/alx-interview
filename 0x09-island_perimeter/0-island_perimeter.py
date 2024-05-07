#!/usr/bin/python3
""" Island perimeter
"""


def island_perimeter(grid):
    """ Return the perimeter of the island
        described in grid """
    perimeter = 0
    width = len(grid[0])
    height = len(grid)

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                perimeter += 4
                if (j > 0 and grid[i][j - 1] == 1):
                    perimeter -= 2
                    # - 2 because it subtract 1 from the current land
                    # and 1 from the land before the current
                if (i > 0 and grid[i - 1][j] == 1):
                    perimeter -= 2
    return perimeter
