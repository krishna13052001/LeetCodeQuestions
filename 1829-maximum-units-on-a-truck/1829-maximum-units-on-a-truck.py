class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxs = sorted(boxTypes, key = lambda x: x[1] , reverse = True)
        total = 0
        i = 0
        while truckSize > 0 and i < len(boxs):
            if truckSize >= boxs[i][0]:
                total += (boxs[i][0] * boxs[i][1])
                truckSize -= boxs[i][0]
            else:
                total += (truckSize * boxs[i][1])
                truckSize = 0
            i += 1
            print(total)
        # 5 
        # 27 + 10 + 50 = 
        return total
        