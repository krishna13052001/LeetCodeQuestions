class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] res = new int[len];
        res[0] = nums[0];
        for(int i = 1; i < len; i++){
            res[i] = res[i-1] * nums[i];
        }
        int product = nums[len - 1];
        res[len - 1] = res[len - 2];
        for(int i= len - 2; i > 0;  i--){
            res[i] = res[i-1] * product;
            product *= nums[i];
        }
        res[0] = product;
        return res;
    }
}