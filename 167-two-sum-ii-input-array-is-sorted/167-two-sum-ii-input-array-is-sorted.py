class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while(i<=j):
            sum = numbers[i] + numbers[j]
            if(sum == target):
                return [i+1,j+1]
            elif(sum < target):
                # here we should increase the sum value to reach target so we increase the slow pointer
                i += 1
            else:
                j -= 1
            