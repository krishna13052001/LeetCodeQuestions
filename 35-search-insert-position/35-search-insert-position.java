class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0, high = nums.length;
        int mid = -1;
        while(low<=high){
            mid = (low+high)/2;
            try{
                if(nums[mid] == target){
                    return mid;
                } else if(nums[mid]<target){
                    low = mid + 1; 
                } else {
                    high = mid - 1;
                }
            } catch(Exception e) {
                return mid;
            }
        }
        return low;
        
    }
}