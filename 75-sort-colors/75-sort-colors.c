

void sortColors(int* nums, int numsSize){
    int low_pointer = 0, mid_pointer = 0, high_pointer = numsSize-1;
    while(mid_pointer<=high_pointer){
        if(nums[mid_pointer] == 0){
            nums[mid_pointer] = nums[low_pointer];
            nums[low_pointer] = 0;
            low_pointer++;
            mid_pointer++;
        } else if(nums[mid_pointer] == 1){
            mid_pointer++;
        } else {
            nums[mid_pointer] = nums[high_pointer];
            nums[high_pointer] = 2;
            high_pointer--;
        }
    }
}