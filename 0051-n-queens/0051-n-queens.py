class Solution:
    def copy_board(self, board):
        new_board = []
        for idx in range(len(board)):
            new_board.append(board[idx][:])
        return new_board
    
    def helper(self, col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            new_board = self.copy_board(board)
            ans.append(new_board)
            return
        
        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[row - col] == 0:
                board[row][col] = "Q"
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[row - col] = 1
                self.helper(col + 1, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
                board[row][col] = "."
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[row - col] = 0

    def solveNQueens(self, n):
        ans = []
        board = [["."] * n for _ in range(n)]
        leftRow = [0] * n
        upperDiagonal = [0] * ( 2 * n  - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        self.helper(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
        for idx in range(len(ans)):
            for jdx in range(len(ans[idx])):
                ans[idx][jdx] = "".join(ans[idx][jdx])
        return ans
