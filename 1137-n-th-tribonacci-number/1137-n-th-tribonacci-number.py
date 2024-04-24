class Solution:
    def tribonacci(self, n: int) -> int:
        first_ele, second_ele, third_ele = 0, 1, 1
        if n == 0:
            return first_ele
        elif n ==.1:
            return second_ele
        elif n == 2:
            return third_ele
        else:
            for i in range(n-2):
                temp = first_ele + second_ele + third_ele
                first_ele = second_ele
                second_ele = third_ele
                third_ele = temp
            return third_ele