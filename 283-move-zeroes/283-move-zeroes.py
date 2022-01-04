class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        while(j<len(nums)):
            while(i<len(nums) and nums[i]!=0):
                i+=1
            if(i==len(nums)):
                break
            else:
                j = i+ 1
                while(j<len(nums) and nums[j]==0):
                    j+=1
                if(j==len(nums)):
                    break
                else:
                    nums[j],nums[i] = nums[i],nums[j]
            i +=1
                
        