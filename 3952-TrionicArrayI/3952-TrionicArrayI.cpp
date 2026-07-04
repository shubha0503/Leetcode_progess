// Last updated: 7/4/2026, 10:40:57 AM
class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        int p = 0;

        // strictly increasing from start
        while (p < n - 2 && nums[p] < nums[p + 1]) {
            p++;
        }
        if (p == 0) return false;

        // strictly decreasing next
        int q = p;
        while (q < n - 1 && nums[q] > nums[q + 1]) {
            q++;
        }
        if (q == p || q == n - 1) return false;

        // strictly increasing to end
        while (q < n - 1 && nums[q] < nums[q + 1]) {
            q++;
        }

        return q == n - 1;
    }
};
