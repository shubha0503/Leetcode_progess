# Last updated: 9/16/2026, 11:59:55 AM
class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s