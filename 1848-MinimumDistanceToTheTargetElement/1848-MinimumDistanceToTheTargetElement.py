# Last updated: 9/16/2026, 11:56:45 AM
class Solution:
  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
    ans = math.inf

    for i, num in enumerate(nums):
      if num == target:
        ans = min(ans, abs(i - start))

    return ans