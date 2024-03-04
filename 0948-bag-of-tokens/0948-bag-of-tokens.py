class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        score = 0
        maxScore = 0
        j = len(tokens) - 1
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                maxScore = max(maxScore, score)
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return maxScore