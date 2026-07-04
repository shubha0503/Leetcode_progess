# Last updated: 7/4/2026, 10:44:06 AM
class Solution:
  def bitwiseComplement(self, n: int) -> int:
    mask = 1
    while mask < n:
      mask = (mask << 1) + 1
    return mask ^ n