class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(nums, k):
            left = right = count = 0
            d = {}
            length = len(nums)
            while right < length:
                if d.get(nums[right],0) == 0:
                    d[nums[right]] = 1
                else:
                    d[nums[right]] += 1
                while len(d) > k and left <= right:
                    d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        del d[nums[left]]
                    left += 1
                count += (right - left +1)
                right += 1
            return count
        return atMost(nums, k) -atMost(nums, k -1)
                