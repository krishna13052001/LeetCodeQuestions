class Solution {
    public int climbStairs(int n) {
        if(n==1 || n==0)
            return 1;
        if(n==2)
            return 2;
        int j = 1,i = 2,newnumber = 0;
        while(n>2){
            newnumber = i + j;
            j = i;
            i = newnumber;
            n -= 1;
        }
        return i;
    }
}