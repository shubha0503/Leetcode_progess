# Last updated: 7/4/2026, 10:44:31 AM
class Solution:
  def maxRotateFunction(self, nums: list[int]) -> int:
    f = sum(i * num for i, num in enumerate(nums))
    ans = f
    summ = sum(nums)

    for a in reversed(nums):
      f += summ - len(nums) * a
      ans = max(ans, f)

    return ans