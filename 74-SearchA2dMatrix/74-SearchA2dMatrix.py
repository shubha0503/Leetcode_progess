# Last updated: 11/25/2026, 7:58:52 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = (row*cols) - 1
        while low <= high:
            mid = (low + high)//2
            if target == matrix[mid//cols][mid %cols] :
                return True
            elif target > matrix[mid//cols][mid %cols]:
                low = mid+ 1
            else:
                high = mid - 1
        return False
