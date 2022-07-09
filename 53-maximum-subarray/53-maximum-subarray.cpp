class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum=nums[0], currSum = 0;
        for(auto i=0;i<nums.size();i++){
            currSum += nums[i];
            if(currSum > maxSum){
                maxSum = currSum;
            }
            if(currSum<0){
                currSum=0;
            }
        }
        return maxSum;
    }
};