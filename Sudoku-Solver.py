"""
	-> We are writing a Sudoku solver 
	-> This entire solver is enclosed in its own class 
	-> We have multiple definitions / methods defined as part of this class
	-> And then right at the end of the .py file, this class is tested by calling the `solve_sudoku` method 
	-> So we are first defining the class for the solver 
"""

class Board:

"""
	-> The Board Class:
		-> This represents the Sudoku game board 
		-> We have methods defined as part of this, to initialise the Sudoku board and display it as a string 
		-> There are other methods set up for this class:
			-> To find an empty cell on the board
			-> To check if a number is valid in a certain row
			-> To check if a number is valid to be placed on the ground
			-> To solve the puzzle recursively, by using backtracking 
"""

    def __init__(self, board):
        self.board = board

"""
    Defining methods as part of this: 
        -> The `__init__` method <- This initialises the `Board` object with a given board configuration 
        -> The `__str__ ` method <- We are drawing a grid for the Sudoku board, created out of strings. This method 
            generates the representation of this 
        -> The `find_empty_cell` method <- This iterates through the Sudoku board and returns the coordinates of an 
            empty cell which we want to populate

        -> We are then defining methods which encode the Sudoku rules onto the board: 
            -> We are checking that the numbers which we want to enter into the board are valid 
            -> There are three methods to do this, which are `valid_in_row`, `valid_in_col`, and `valid_in_square`
            -> To make sure that we can place the number we are trying to enter into a column, row or square in the grid 

        -> We then define a method (`is_valid`), to check that a number can be placed inside a cell on the grid 
            -> We can't have numbers repeated in the same row, column or square <- this method encodes this
            
        -> The final method defined as part of this solves the Sudoku puzzle, by recursively attempting to enter numbers 
            1-9 in different cells on the board and seeing if these are valid placements or not
            -> This is done with the `solver` method  and uses backtracking  
"""

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start=(col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

"""
    We then define the `solve_sudoku` function:
        -> This creates a `Board` object, to create a Sudoku board out of the given numbers 
        -> Then printing this initial puzzle, attempting to solve it and printing out the solution if we find one

    Then defining `puzzle`:
        -> This defines the Sudoku puzzle as a list of lists
        -> Each of these inner lists represents a row of the board 

    Testing the function:
        -> We are then calling the `solve_sudoku` function, with the input puzzle
        -> This solves the function with a brute force approach 
        -> We are trying different numbers in empty cells again and again until something words, according to the 
            Sudoku rules we have coded 
        -> It this brute force approach doesn't work, then we are concluding that the puzzle which has been input into 
            the function can't be solved
"""

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)

    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)
