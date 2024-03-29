class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = -1
        length = len(nums)
        for num in nums:
            if num > maxi:
                maxi = num
       
        d = {}
        maxiCounter = 0
        ans = left = right =0
        while right < length:
            if nums[right] == maxi:
                maxiCounter += 1
            while maxiCounter >= k :
                ans += length - right
                if nums[left] == maxi:
                    maxiCounter -=1
                left += 1
            right += 1
        return ans