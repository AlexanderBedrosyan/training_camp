import random

class Board:

    def __init__(self):
        self.board = []
        self.rows = None
        self.columns = None

    def add_matrix_to_the_board(self, rows, cols):
        self.rows = rows
        self.columns = cols
        for _ in range(rows):
            current_row = []
            for _ in range(cols):
                current_row.append(0)

            self.board.append(current_row)

    def show_current_board(self):
        for row in self.board:
            print(*row)

    def add_mines_on_the_board(self, number_of_mines):
        while number_of_mines:

            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.columns - 1)

            if self.board[row][col] != '*':
                self.board[row][col] = '*'
                number_of_mines -= 1

    def is_valid(self, current_row, current_col):
        if current_row < 0 or current_col < 0 or current_row >= self.rows or current_col >= self.columns:
            return False
        return True

    def mines_checker(self, current_row, current_col):
        if not self.is_valid(current_row, current_col):
            return 0
        if self.board[current_row][current_col] == "*":
            return 1
        return 0


    def count_numbers_of_mines_around(self, current_row, current_col):
        counter = 0
        counter += self.mines_checker(current_row + 1, current_col)
        counter += self.mines_checker(current_row - 1, current_col)
        counter += self.mines_checker(current_row, current_col - 1)
        counter += self.mines_checker(current_row, current_col + 1)
        counter += self.mines_checker(current_row - 1, current_col - 1)
        counter += self.mines_checker(current_row - 1, current_col + 1)
        counter += self.mines_checker(current_row + 1, current_col - 1)
        counter += self.mines_checker(current_row + 1, current_col + 1)
        return counter


    def add_numbers_on_the_board(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == "*":
                    continue
                self.board[row][col] = self.count_numbers_of_mines_around(row, col)


board = Board()
board.add_matrix_to_the_board(4, 4)
board.add_mines_on_the_board(3)
board.add_numbers_on_the_board()
board.show_current_board()
