# Last updated: 9/16/2026, 11:55:40 AM
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for x in asteroids:
            if mass < x:
                return False
            mass += x
        return True