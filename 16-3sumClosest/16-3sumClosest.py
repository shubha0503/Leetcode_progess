# Last updated: 7/4/2026, 10:45:52 AM
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # Update closest sum
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1

        return closest