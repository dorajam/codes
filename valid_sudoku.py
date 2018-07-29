"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Notes:
1. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
2. Only the filled cells need to be validated according to the mentioned rules.
3. The given board contain only digits 1-9 and the character '.'.
4. The given board size is always 9x9.

July, 2018 Dora Jambor
Problem described on https://leetcode.com/problems/valid-sudoku/description/
"""

def is_valid(board):
    for ls in board:
        seen = []
        for e in ls:
            if e == '.':
                continue
            if e not in seen:
                seen.append(e)
            else:
                return False
    return True

def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    swopped_board = []
    for i in range(len(board[0])):
         subls = []
         for ls in board:
             subls += [ls[i]]
         swopped_board.append(subls)

    subboxes = []
    for outer in [0,3,6]:
        for idx in [0,3,6]:
            subls = []
            for row in board[outer:outer+3]:
                subls +=row[idx:idx+3]
            subboxes.append(subls)

    return is_valid(board) & is_valid(swopped_board) & is_valid(subboxes)

example1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

example2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print is_valid_sudoku(example1)
print is_valid_sudoku(example2)
