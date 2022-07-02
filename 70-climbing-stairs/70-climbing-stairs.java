class Solution {
    public int result(int n, int []dp){
        if (n==0 || n==1){
            dp[n] = 1;
            return dp[n];
        }
        if(dp[n] != -1){
            return dp[n];
        }
        dp[n] = result(n-1,dp) + result(n-2,dp);
        System.out.println(Arrays.toString(dp));
        return dp[n];
    }
    public int climbStairs(int n) {
        int[] dp = new int[n+1];
        for (int i=0;i<n+1;i++){
            dp[i] = -1;
        }
        return result(n,dp);
    }
}