# Last updated: 9/16/2026, 11:54:28 AM
class Solution:
  def furthestDistanceFromOrigin(self, moves: str) -> int:
    return abs(moves.count('L') - moves.count('R')) + moves.count('_')