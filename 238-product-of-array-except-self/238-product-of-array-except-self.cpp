class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> res(length, 1);
        res[0] = nums[0];
        for(int i = 1 ; i < length; i++){
            res[i] = res[i-1] * nums[i];
        }
        int product = nums[length - 1];
        res[length - 1] = res[length - 2];
        for(int i= length -2; i>0; i--){
            res[i] = res[i-1] * product;
            product *= nums[i];
        }
        res[0] = product;
        return res;
    }
};