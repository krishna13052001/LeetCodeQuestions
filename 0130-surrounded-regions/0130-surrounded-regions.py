class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        def dfs(row, col):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            print(row, col)
            visited[row][col] = True
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and not visited[nr][nc]:
                    dfs(nr, nc)
        for rdx in range(rows):
            if board[rdx][0] == "O" and not visited[rdx][0]:
                print("1")
                dfs(rdx, 0)
            if board[rdx][-1] == "O" and not visited[rdx][-1]:
                print("2", rdx, cols - 1)
                dfs(rdx, cols - 1)
        for cdx in range(cols):
            if board[0][cdx] == "O" and not visited[0][cdx]:
                print("3")
                dfs(0, cdx)
            if board[-1][cdx] == "O" and not visited[-1][cdx]:
                print("4")
                dfs(rows - 1, cdx)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and not visited[row][col]:
                    board[row][col] = "X"

    
        