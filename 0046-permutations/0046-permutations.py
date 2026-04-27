class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result, path = [], []
        visited = [False] * n
        
        def backtrack(idx: int):
            if idx == n:
                result.append(path[:])
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtrack(idx + 1)
                    path.pop()
                    visited[i] = False
        
        backtrack(0)
        return result