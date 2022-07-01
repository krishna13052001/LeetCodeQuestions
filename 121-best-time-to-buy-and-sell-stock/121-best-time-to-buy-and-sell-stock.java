class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        int min_value = Integer.MAX_VALUE;
        for(int i = 0; i< prices.length ; i++){
            min_value = min_value < prices[i] ? min_value : prices[i];
            profit = profit < prices[i] - min_value ? prices[i] - min_value : profit;
        }
        return profit;
    }
}