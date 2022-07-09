class Solution {
    public int majorityElement(int[] nums) {
        int count = 1, majority = nums[0];
        for(int i = 0; i< nums.length; i++){
            if(nums[i] != majority){
                count -= 1;
                if(count == 0){
                    count = 1;
                    majority = nums[i];
                }
            } else {
                count += 1;
            }
        }
        return majority;
    }
}