# Last updated: 7/4/2026, 10:42:17 AM
class Solution:
  def twoEditWords(
      self,
      queries: list[str],
      dictionary: list[str],
  ) -> list[str]:
    return [query for query in queries
            if any(sum(a != b for a, b in zip(query, word)) < 3
                   for word in dictionary)]