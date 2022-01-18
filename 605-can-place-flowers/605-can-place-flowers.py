class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        i = 0
        prev = 0
        nxt = 0
        while(i<length and n != 0):
            if(i == length -1):
                nxt = 0
            else:
                nxt = flowerbed[i+1]
            # print(prev,nxt)
            if(flowerbed[i] == 0 and prev == 0 and nxt ==0):
                n -= 1
                flowerbed[i] = 1
            prev = flowerbed[i]
            i += 1
            # print(flowerbed,prev,nxt)
        if(n==0):
            return True
        return False
            