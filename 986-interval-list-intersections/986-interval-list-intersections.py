class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        apointer , bpointer = 0,0
        lengthA,lengthB = len(firstList),len(secondList)
        while(apointer<lengthA and bpointer<lengthB):
            if(secondList[bpointer][0]<=firstList[apointer][1] and firstList[apointer][0]<=secondList[bpointer][1]):
                res.append([max(firstList[apointer][0],secondList[bpointer][0]),min(firstList[apointer][1],secondList[bpointer][1])])
            if(firstList[apointer][1]>secondList[bpointer][1]):
                bpointer += 1
            else:
                apointer += 1
        return res