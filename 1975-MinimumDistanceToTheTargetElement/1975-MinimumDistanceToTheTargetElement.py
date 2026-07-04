# Last updated: 7/4/2026, 10:42:50 AM
class Solution:
  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
    ans = math.inf

    for i, num in enumerate(nums):
      if num == target:
        ans = min(ans, abs(i - start))

    return ans