// Last updated: 7/4/2026, 10:45:40 AM
int removeElement(int* nums, int numsSize, int val) {
    int k = 0; 
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            nums[k++] = nums[i];
        }
    }
    return k;
}