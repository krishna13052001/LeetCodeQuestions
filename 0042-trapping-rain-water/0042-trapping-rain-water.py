class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        sum = 0
        maxleft, maxright = height[left],height[right]
        while (left < right):
            if maxleft <= maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                sum += (maxleft - height[left])
            else:
                right -= 1
                maxright = max(maxright, height[right])
                sum += (maxright - height[right])
        return sum