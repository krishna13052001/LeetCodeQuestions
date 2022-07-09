class Solution {
    public void sortColors(int[] nums) {
        int len = nums.length;
        int low = 0, mid = 0, high = len - 1,temp=0;
        while(mid <= high){
            if(nums[mid] == 0){
                temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;
                low++;
                mid++;
            } else if(nums[mid] == 1){
                mid++;
            } else {
                temp = nums[high];
                nums[high] = nums[mid];
                nums[mid] = temp;
                high--;
            }
        }
    }
}