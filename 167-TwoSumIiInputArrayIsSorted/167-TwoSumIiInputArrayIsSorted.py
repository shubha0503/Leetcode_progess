# Last updated: 11/25/2026, 7:58:19 PM
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for num in numbers:
            x = target - num
            if x in numbers:
                if numbers.index(num) != numbers.index(x):
                    return numbers.index(num)+1,numbers.index(x)+1
                else:
                    return numbers.index(num)+1,numbers.index(x)+2