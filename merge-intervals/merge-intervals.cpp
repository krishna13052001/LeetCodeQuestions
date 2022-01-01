class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        vector<int> temp;
        if(intervals.size() == 0){
            return ans;
        }
        sort(intervals.begin(),intervals.end());
        temp = intervals[0];
        for(auto pair:intervals){
            if(pair[0] <= temp[1]){
                temp[1] = max(pair[1],temp[1]);
                // temp[0] = min(pair[0],temp[0]);
            } else {
                ans.push_back(temp);
                temp = pair;
            }
        }
        ans.push_back(temp);
        return ans;
    }
};