# Last updated: 7/4/2026, 10:41:52 AM
class Solution:
  def furthestDistanceFromOrigin(self, moves: str) -> int:
    return abs(moves.count('L') - moves.count('R')) + moves.count('_')