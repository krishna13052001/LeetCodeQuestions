from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, color):
        
        original = image[sr][sc]
        if original == color:
            return image
        
        rows, cols = len(image), len(image[0])
        q = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        q.append((nr,nc))
        
        return image