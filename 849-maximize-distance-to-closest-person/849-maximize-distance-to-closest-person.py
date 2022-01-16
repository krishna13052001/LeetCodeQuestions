class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        person = None
        i = 0
        length = len(seats)
        while(i<length and person == None):
            if(seats[i] == 1):
                person = i
                continue
            i += 1
        res = max(person - 0,res)
        for j in range(i+1,length):
            if(seats[j] == 1):
                res = max(res,(j-person)//2)
                person = j
        if(seats[-1] != 1):
            res = max(res,(length-person-1))
        return res