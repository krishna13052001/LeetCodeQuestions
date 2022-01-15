class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_sum = 0
        min_dis = 1<<32
        print(min_dis)
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while(j<k):
                l = [nums[i],nums[j],nums[k]]
                if(min_dis>abs(target-sum(l))):
                    min_sum = sum(l)
                    if(sum(l)==target):
                        return min_sum
                    min_dis = abs(target-min_sum)
                elif(sum(l)>target):
                    k -= 1
                else:
                    j += 1
        return min_sum