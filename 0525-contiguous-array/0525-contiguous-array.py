class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        longest_sum_array_length = 0
        sum_of_values = 0
        d = {}
        for i in range(len(nums)):
            if nums[i] ==0 :
                sum_of_values -= 1
            else:
                sum_of_values += 1
            if sum_of_values == 0:
                longest_sum_array_length = i + 1
            elif d.get(sum_of_values, -1 ) != -1:
                longest_sum_array_length = max(longest_sum_array_length, i - d[sum_of_values])
            else:
                d[sum_of_values] = i
        return longest_sum_array_length