class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int i=0, j = numbers.size() - 1,sum = 0;
        while(i<=j){
            sum = numbers[i] + numbers[j];
            if(sum == target){
                res.push_back(++i);
                res.push_back(++j);
                return res;
            } else if(sum < target){
                i += 1;
            } else {
                j -= 1;
            }
        }
        return res;
    }
};