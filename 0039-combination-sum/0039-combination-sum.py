class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i: int, path: List[int], cur_sum: int):
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target or i == len(candidates):
                return
            
            backtrack(i + 1, path, cur_sum)
            path.append(candidates[i])
            backtrack(i, path, cur_sum + candidates[i])
            path.pop()
        
        candidates.sort()
        backtrack(0, [], 0)
        return res
