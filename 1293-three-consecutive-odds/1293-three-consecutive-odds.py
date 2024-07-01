class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window = 0
        for i in range(min(3, len(arr))):
            window += arr[i] % 2
        if window == 3:
            return True
        for i in range(3, len(arr)):
            window += arr[i] % 2
            window -= arr[i - 3] % 2
            if window == 3:
                return True
        return False