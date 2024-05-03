class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_of_rolles = sum(rolls)
        sum_of_mean_rolles = mean *(len(rolls) + n)
        total = sum_of_mean_rolles - sum_of_rolles
        if total < n or total > 6 * n:
            return []
        else:
            res = []
            while total:
                dice = min(total -n +1, 6)
                res.append(dice)
                total -= dice
                n -= 1
            return res
