class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [i+1 for i in range(n)]
        self.get_combination(k,nums,[],result)
        return result
    def get_combination(self,k,nums,current,result):
        if(len(current) == k):
            result.append(current)
        elif(len(current)+len(nums)<k):
            return
        for idx,val in enumerate(nums):
            self.get_combination(k,nums[idx+1:],current+[val],result)