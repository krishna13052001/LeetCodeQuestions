import sys
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        length = len(gas)
        total ,res = 0,0
        index = 0
        for i in range(length):
            total += (gas[i]-cost[i])
            if(total<0):
                total = 0
                index = (i + 1)%length
        print(gas)
        return index