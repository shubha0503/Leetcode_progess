# Last updated: 9/16/2026, 11:54:22 AM
class Solution:
  def areSimilar(self, mat: list[list[int]], k: int) -> bool:
    n = len(mat[0])
    for row in mat:
      for j in range(n):
        if row[j] != row[(j + k) % n]:
          return False
    return True