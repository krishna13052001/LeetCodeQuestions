class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = {} 
        for ele in nums3:
            for el in nums4:
                d[ele+el] = d.get(ele+el,0)+1
        count = 0
        for ele in nums1:
            for el in nums2:
                count += d.get(-(ele+el),0)
        return count