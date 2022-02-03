class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if(len(nums)<k):
            return -1
        count =0
        for i in range(k):
            count += nums[i]
        low = 0
        high = k-1
        res = count/k
        length = len(nums)
        while(high<length):
            count -= nums[low]
            low += 1
            high += 1
            if(high>=length):
                break
            count += nums[high]
            res= max(res,count/k)
        return res