import sys


class GameOfLife:
    """Game Of Life

    The grid is made up of a 2D array of integers. '0' is a dead cell, '1' is a live cell.

    Attributes:
      width (int)
      height (int)
    """
    def __init__(self, width, height):
        # initialize new grid full of 0's
        self.grid = [[0 for row in xrange(width)] for col in xrange(height)]
        self.width = width
        self.height = height

    # set grid for testing purposes
    def set_grid(self, new_grid):
        assert len(new_grid) == self.height
        assert len(new_grid[0]) == self.width
        self.grid = new_grid

    def print_grid(self):
        print "-" * (self.width * 3 - 2)
        for line in self.grid:
            for cell in line:
                if cell == 0:
                    sys.stdout.write('.  ')
                else:
                    sys.stdout.write('x  ')
            # print a new line
            print

    def iterate(self):
        """Iterate the grid accorinding to game of life rules.

        If the cell is alive, it stays alive if it has either 2 or 3 live neighbors.
        If the cell is dead, it comes to life only if it has 3 live neighbors.
        """
        # initialize new grid full of 0's
        new_grid = [[0 for row in xrange(self.width)] for col in xrange(self.height)]
        for row in xrange(self.height):
            for col in xrange(self.width):
                cell = self.grid[row][col]
                neighbors = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # don't append self as neighbor
                        if i != 0 or j != 0:
                            # modulus the index for it to wrap around properly at the edge
                            neighbors.append(self.grid[(row + i) % self.height][(col + j) % self.width])
                neighbors_alive = 0
                for n in neighbors:
                    if n == 1:
                        neighbors_alive += 1
                if cell == 1:
                    if neighbors_alive < 2 or neighbors_alive > 3:
                        new_grid[row][col] = 0
                    else:
                        new_grid[row][col] = 1
                if cell == 0:
                    if neighbors_alive == 3:
                        new_grid[row][col] = 1
                    else:
                        new_grid[row][col] = 0
        self.grid = new_grid


if __name__ == '__main__':
    game = GameOfLife(9, 10)
    # let's use a "glider" to test rotation and translation (and wrap around)
    glider_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    game.set_grid(glider_grid)
    game.print_grid()
    while True:
        raw_input("Press [enter] to iterate")
        game.iterate()
        game.print_grid()

