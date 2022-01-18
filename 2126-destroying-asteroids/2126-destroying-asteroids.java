class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        long count = mass;
        for(int val : asteroids){
            if(count < (long)val){
                return false;
            } else {
                count += val;
            }
        }
        return true;
    }
}