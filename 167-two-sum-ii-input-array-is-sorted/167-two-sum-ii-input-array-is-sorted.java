class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0,j=numbers.length-1;
        int[] res = new int[2];
        int sum = 0;
        while(i<=j){
            sum = numbers[i] + numbers[j];
            if(sum == target){
                res[0] = i+1;
                res[1] = j+1;
                return res;
            } else if(sum < target){
                i += 1;
            } else {
                j -= 1;
            }
        }
        return res;
    }
}