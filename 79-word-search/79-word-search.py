class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,-1),(-1,0),(1,0),(0,1)]
        m,n=len(board),len(board[0])
        # visited = [[False]*m]*n
        visited = defaultdict(lambda: defaultdict(bool))
        for i in range(m):
            for j in range(n):
                if(board[i][j] == word[0]):
                    if self.dfs(board,word,dirs,i,j,visited,1):
                        return True
        return False
    
    def dfs(self,board,word,dirs,i,j,visited,index):
        visited[i][j] = True
        if(index >= len(word)):
            return True
        m = len(board)
        n = len(board[0])
        for dx,dy in dirs:
            I = i + dx
            J = j + dy
            if(I>=0 and I<m) and (J>=0 and J<n) and visited[I][J] == False and board[I][J] == word[index]:
                if self.dfs(board,word,dirs,I,J,visited,index+1):
                    return True
        visited[i][j] = False 
        return False