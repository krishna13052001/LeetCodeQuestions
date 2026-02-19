class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0, len(height) - 1
        rightMax = leftMax = 0
        result = 0
        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    result += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if rightMax > height[right]:
                    result += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return result