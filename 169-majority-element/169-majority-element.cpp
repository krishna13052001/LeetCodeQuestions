class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority = nums[0], count =1;
        for(int i = 1; i<nums.size();i++){
            if(nums[i] != majority){
                count--;
                if(count == 0){
                    count = 1;
                    majority = nums[i];
                }
            } else {
                count++;
            }
        }
        return majority;
    }
};