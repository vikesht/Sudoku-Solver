class SudokuSolver:
    def __init__(self):
        print("enter each row on a new line, values seperated by space and use '.' to represent empty cell ")
        self.board = []
        for _ in range(8):
            self.board.append(input().split())
        # print(self.board)
        t = self.solveSudoku()
        if t :
            print("Solution is :")
            for i in self.board:
                print(*i)
        else:
            print("solution does not exist")

    def solveSudoku(self) :
        x = ['1', '2', '3', '4', '5', '6', '7', '8']
        def solve():
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == '.':
                        for k in x:
                            if isvalid(k, i, j):
                                self.board[i][j] = k
                                if solve() == True:
                                    return True
                                else:
                                    self.board[i][j] = '.'
                        return False
            return True
        def isvalid(c, row, col):
            for i in range(8):
                if self.board[row][i] == c:
                    return False
                if self.board[i][col] == c:
                    return False
                if self.board[2 * (row//2)  + i //4][4* (col//4)+ i %4] == c:
                    return False
            return True

        return  solve()

SudokuSolver()
