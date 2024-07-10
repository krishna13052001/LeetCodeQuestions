class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log[0] != ".":
                count += 1
            elif log[0] == "." and log[1] == "." and count > 0:
                count -= 1
            else:
                pass
        return count
