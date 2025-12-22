class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        count = 0
        for idx, num in enumerate(nums):
            count += num
            rem = count % k
            if rem in d:
                if idx - d[rem] > 1:
                    return True
            else:
                d[rem] = idx
        return False