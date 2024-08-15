class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_of_fives = 0
        no_of_tens = 0
        for bill in bills:
            if bill == 5:
                no_of_fives += 1
            elif bill == 10 and no_of_fives >= 1:
                no_of_tens += 1
                no_of_fives -= 1
            elif bill == 20:
                if no_of_fives >=1 and no_of_tens>=1:
                    no_of_fives -= 1
                    no_of_tens -= 1
                elif no_of_fives >= 3:
                    no_of_fives -= 3
                else:
                    return False
            else:
                return False
        return True
