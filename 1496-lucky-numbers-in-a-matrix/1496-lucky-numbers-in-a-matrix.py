class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            idx = matrix[i].index(min(matrix[i]))
            for j in range(len(matrix)):
                if(matrix[j][idx] > matrix[i][idx]):
                    break
                if(j == len(matrix) - 1):
                    ans.append(matrix[i][idx])
        return ans
                