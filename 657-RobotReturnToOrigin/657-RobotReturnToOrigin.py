# Last updated: 7/4/2026, 10:44:24 AM
class Solution:
  def judgeCircle(self, moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')