class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)
        mid = -1
        while(low<=high):
            mid = (low+high)//2
            try:    
                if(nums[mid] == target):
                    print("hig")
                    return mid
                elif(nums[mid]<target):
                    low = mid+1
                else:
                    high=mid-1
            except:
                print("hi")
                return mid
        print("hello")
        return low
        