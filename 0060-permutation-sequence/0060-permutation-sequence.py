class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        factoral = 1
        numbers = []
        for i in range(1, n):
            factoral *= i
            numbers.append(i)
        numbers.append(n)
        k = k - 1
        while True:
            idx = k // factoral
            res += str(numbers[idx])
            numbers.pop(idx)
            if len(numbers) == 0:
                break
            k = k % factoral
            factoral //= len(numbers)
        return res