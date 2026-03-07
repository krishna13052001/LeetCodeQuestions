class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, arr, target, subarray):
            if target == 0:
                res.append(subarray[:])
                return
            for i in range(idx, len(arr)):
                if i > idx and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                subarray.append(arr[i])
                backtrack(i + 1, arr, target - arr[i], subarray)
                subarray.pop()
        backtrack(0, candidates, target, [])
        return res