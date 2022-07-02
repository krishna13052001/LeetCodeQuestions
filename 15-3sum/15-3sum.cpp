class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int length = nums.size();
        vector<vector<int>> res;
        if (length < 3){
            return res;
        }
        sort(nums.begin(),nums.end());
        for(int i=0;i<length-2; ++i){
            if (i == 0 || nums[i] != nums[i-1]){
                int j = i+1,k=length -1;
                while(j<k){
                    int sum = nums[i] + nums[j] + nums[k];
                    if(sum == 0){
                        // vector<int> v1{nums[i],nums[2]}
                        res.push_back({nums[i],nums[j],nums[k]});
                        while(j<k && nums[j] == nums[j+1]){
                            j += 1;
                        }
                        while(j<k && nums[k] == nums[k-1]){
                            k -= 1;
                        }
                        j++;
                        k--;
                    } else if(sum < 0){
                        j += 1;
                    } else {
                        k -= 1;
                    }
                }
            }
        }
        return res;
    }
};