class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0, len(height) -1
        maxi = 0
        while left < right:
            maxi = max(maxi, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxi