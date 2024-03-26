class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates,0,[],0,target,res)
        return res
    def dfs(self,candidates,i,cur,cur_sum,target,res):
        if(cur_sum == target):
            res.append(list(cur))
            return
        if(cur_sum > target or i >= len(candidates)):
            return
        
        self.dfs(candidates,i+1,cur,cur_sum,target,res)
        cur.append(candidates[i])
        cur_sum += candidates[i]
        self.dfs(candidates,i,cur,cur_sum,target,res)
        cur.pop()
        cur_sum -= candidates[i]