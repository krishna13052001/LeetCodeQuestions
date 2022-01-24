class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)
        for i in range(length-3):
            for j in range(i+1,length-2):
                k = j+1
                l = length-1
                while(k<l):
                    count = nums[i]+nums[j]+nums[k]+nums[l]
                    if( count == target):
                        ans = [nums[i],nums[j],nums[k],nums[l]]
                        if(ans not in res):
                            res.append(ans)
                        k += 1
                        l-=1
                    elif(count < target):
                        k += 1
                    else:
                        l-=1
                    # print(res,k,l)
        return res