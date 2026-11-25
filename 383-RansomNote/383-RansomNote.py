# Last updated: 11/25/2026, 7:57:48 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,"",1)
            else:
                return False
        return True