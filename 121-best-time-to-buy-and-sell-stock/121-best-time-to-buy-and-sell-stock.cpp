class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit;
        int min_value = INT_MAX;
        for (auto& it : prices) {
            min_value = min_value < it ? min_value : it;
            profit = profit < it - min_value ? it - min_value : profit;
        }
        return profit;
    }
};