class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1, mid = 0, left_value, mid_value;
        while(low <= high){
            mid = (low + high) / 2;
            left_value = nums[low];
            mid_value = nums[mid];
            if(mid_value == target){
                return mid;
            } else if((left_value < mid_value && (left_value <= target && target < mid_value)) ||
                  (left_value > mid_value && (target < mid_value || target >= left_value))){
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }
};