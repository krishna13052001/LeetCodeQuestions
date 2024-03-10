class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            d[i] = 1
        res = {}
        for i in nums2:
            if d.get(i, -1) != -1:
                res[i] = 1
        return list(res.keys())