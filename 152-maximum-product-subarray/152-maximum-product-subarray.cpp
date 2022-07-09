class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxi=nums[0], mins = nums[0], prod = nums[0],temp;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] < 0){
                temp = maxi;
                maxi = mins;
                mins = temp;
            }
            maxi = max(nums[i],maxi*nums[i]);
            mins = min(nums[i],mins*nums[i]);
            prod = max(prod,maxi);
        }
        return prod;
    }
};