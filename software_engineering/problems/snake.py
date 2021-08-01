"""Libraries to implement the game of snake"""
from matrix_ops import rotate_counterclockwise, rotate_clockwise
import time
import os

clear = lambda: os.system('clear')

class Snake:
  """A snake who lives on a Board instance."""
  def __init__(self, x_pos, y_pos, direction="R", starting_length=5):
    """Initialize a snake object"""
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.body = [(x_pos, y_pos) for _ in range(starting_length)]
    self.direction = direction
    self.offset_map = {
      'U': (0, 1),
      'D': (0, -1),
      'L': (-1, 0),
      'R': (1, 0)
    }

  def move(self, direction):
    """
    Every segment of the snake's body follows where the segment in
    front of it goes. Direction is defined by segments, in order, from the
    head which is always stored at the end of the "body" list.
    """
    print(self.body[::-1])
    self.direction = direction
    offset = self.offset_map[direction]

    new_head = (self.body[0][0] + offset[0], self.body[0][1] + offset[1])
    old_head = (self.body[0][0], self.body[0][1])

    body = [new_head]
    # Python lists are implemented as heaps, so we have to make another data structure, or,
    # play with index swapping.
    for i in range(1, len(self.body)):
      body.append(old_head)
      old_head = self.body[i]

    self.body = body
    print(self.body[::-1])

  def eat(self, amount):
    """The snake eats, and adds a segment on its next movement."""
    for _ in range(amount):
      self.body.append(self.body[-1])

class Board:
  """An object representing the game board"""
  def __init__(self, height, width):

    if height < 10 or height > 100:
      print(("Height specified: {}, is outside the allowed range"
           " [10, 100]. Using default height of 40").format(height))
      height = 40
    if width < 10 or width > 100:
      print(("Width specified: {}, is outside the allowed range"
           " [10, 100]. Using default width of 40").format(width))
      width = 40

    self.height = height
    self.width = width
    self.snakes = []
    
    # Create the board
    #
    # For ease of reading, we want the board-position to be accessed using
    # cartesian coordinates, e.g. [X][Y]. We will represent the board as a 2D
    # list, where the row-dimension is first, and the column dimension is
    # second. The board will be bordered by 'X' characters for easy of viewing.
    # This also sets a character encoding for different types of entities on the
    # board. The indexing of the list means that it will print "sideways"
    self.board = [['X' for _ in range(self.height + 2)]]
    for __ in range(self.width):
      self.board.append(['X'] + [' ' for _ in range(self.height)] + ['X'])
    self.board.append(['X' for _ in range(self.height + 2)])
    
  def get_board_state(self):
    """
    Prints the board to the console, with the board-index for horizontal
    and vertical position starting from 0, 0 from the bottom left, and
    increasing positively from left to right.
    
    A 10x5 board with a snake on it might look like this:
    
    XXXXXXXXXXX
    X     SSS X
    X  SS S   X
    X   SSS   X
    X         X
    XXXXXXXXXXX
    
    The board is returned as a multiline string to ensure the coordinates are
    represented properly.
    
    Returns:
      mulitline character encoding of the board, snakes, and food.
    """
    
    board_state = []
    
    out_board = rotate_counterclockwise(self.board)
    for row in out_board:
      board_state.append(''.join(row))
    # Reverse order to orient the "origin" correctly.
    board_state = '\n'.join(board_state)
      
    return board_state
  
  def show_console_board(self):
    """
    Prints the board state the console. Printing assumes that we are in a game
    loop, so uses carridge returns to clear the console and print over what was
    already there.
    """
    print(self.get_board_state())

  def generate_food(self):
    """Create a lovely morsel of food for the snake to eat"""
    pass

class Game:
  """Give the game a board, and some snakes"""
  def __init__(self):
    pass

  def add_board(self):
    """Give the game state a board"""
    pass

  def add_snake(self):
    """Add a snake to the board"""
    pass

  def collision_check(self):
    """Check if any collisions have occurred"""
    pass

  def run(self):
    """Run the game until all snakes are dead"""
    pass

if __name__ == '__main__':
  clear()
  board = Board(height=15, width=30)
  board.show_console_board()
  time.sleep(0.5)
  clear()
  board.board[5][5] = 'S'
  board.show_console_board()
  time.sleep(0.5)
  clear()
  board.board[6][5] = 'S'
  board.board[5][5] = ' '
  board.show_console_board()
  time.sleep(0.5)
  clear()
  board.board[6][5] = ' '
  board.board[7][5] = 'S'
  board.show_console_board()
