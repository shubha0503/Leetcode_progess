# Last updated: 7/4/2026, 10:44:13 AM
class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in s + s