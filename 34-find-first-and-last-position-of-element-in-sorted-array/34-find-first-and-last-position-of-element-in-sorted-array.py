class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            if(nums[mid]==target):
                res[0] = mid
                high = mid-1
            elif(nums[mid]<target):
                low = mid+1
            else:
                high = mid -1
        low = 0
        if(res[0] != -1):
            low= res[0]
        high = len(nums)-1
        while(low<=high):
            mid = (low+high)//2
            print(mid)
            if(nums[mid]==target):
                res[1] = mid
                low = mid+1
                print(low,len(nums))
            elif(nums[mid]<target):
                low = mid + 1
            else:
                high = mid-1
        return res