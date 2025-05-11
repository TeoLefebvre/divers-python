import numpy as np
from copy import deepcopy

def print_sudoku(sudoku):
    for i in range(9):
        if i == 3 or i == 6:
            print('='*23)
        for j in range(9):
            if j == 3 or j == 6:
                print('||', end=' ')
            c = sudoku[i,j]
            if c == 0:
                print('_', end=' ')
            else:
                print(c, end=' ')
        print()
    print()

def solve_sudoku(sudoku: np.ndarray):
    sudoku = deepcopy(sudoku)
    numbers = []
    to_complete = np.sum(sudoku == 0)
    i, j = 0,0
    forward = True
    while len(numbers) < to_complete:
        display = True
        if forward:
            # find next empty
            while sudoku[i,j]:
                j += 1
                if j == 9:
                    j = 0
                    i += 1

            # verify possibilities
            possibilities = set(range(1,10))
            line = sudoku[i,:]
            column = sudoku[:,j]
            si, sj = i//3, j//3
            square = sudoku[3*si:3*(si+1),3*sj:3*(sj+1)]
            possibilities -= set(line)
            possibilities -= set(column)
            possibilities -= set(square.flatten())

            if len(possibilities):
                # append a number if there is possibilities
                iterator = iter(possibilities)
                sudoku[i,j] = next(iterator)
                numbers.append(((i,j), iterator))
            else:
                # go back to previous number if no possibilities
                forward = False
                display = False
        else:
            (i,j), iterator = numbers[-1]
            try:
                sudoku[i,j] = next(iterator)
                forward = True
            except StopIteration:
                sudoku[i,j] = 0
                numbers.pop()
    return sudoku

def verify_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            c = sudoku[i,j]
            if c == 0:
                return i,j
            line1 = sudoku[i,:j]
            line2 = sudoku[i,j+1:]
            column1 = sudoku[:i,j]
            column2 = sudoku[i+1:,j]
            if c in line1 or c in line2 or c in column1 or c in column2:
                return i,j
    return True

def main():
    sudoku = np.zeros((9,9), dtype=np.int32)
    sudoku[0,2] = 9
    sudoku[0,5] = 7
    sudoku[0,8] = 4
    sudoku[1,3] = 5
    sudoku[1,5] = 4
    sudoku[1,6] = 3
    sudoku[2,8] = 5
    sudoku[3,0] = 5
    sudoku[3,1] = 4
    sudoku[3,2] = 7
    sudoku[4,1] = 3
    sudoku[4,7] = 6
    sudoku[5,1] = 9
    sudoku[5,7] = 3
    sudoku[5,8] = 2
    sudoku[6,2] = 1
    sudoku[6,3] = 3
    sudoku[7,4] = 2
    sudoku[7,6] = 1
    sudoku[7,7] = 8
    sudoku[8,0] = 7
    sudoku[8,4] = 9

    print_sudoku(sudoku)
    solved = solve_sudoku(sudoku)
    print('Ok' if verify_sudoku(solved) else 'Error')
    print_sudoku(solved)

if __name__=="__main__":
    main()