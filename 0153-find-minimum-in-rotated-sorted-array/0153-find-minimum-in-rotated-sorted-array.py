class Solution:
    def findMin(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
    
        if arr[left] < arr[right]:
            return arr[left]

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[mid + 1]:
                return arr[mid + 1]

            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid

        return arr[left]