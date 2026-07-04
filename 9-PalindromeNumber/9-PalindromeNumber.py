# Last updated: 7/4/2026, 10:46:07 AM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str1 = str(x)
        if str1 == str1[::-1]:
           return True
        else:
           return False


        