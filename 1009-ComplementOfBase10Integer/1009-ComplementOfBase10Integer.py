# Last updated: 9/16/2026, 11:59:23 AM
class Solution:
  def bitwiseComplement(self, n: int) -> int:
    mask = 1
    while mask < n:
      mask = (mask << 1) + 1
    return mask ^ n