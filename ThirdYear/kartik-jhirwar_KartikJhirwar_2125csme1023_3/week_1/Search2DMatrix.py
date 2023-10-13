class Solution:
    def searchMatrix(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])
        low, high = 0, r * c - 1
        
        while low <= high:
            mid = (low + high) // 2
            x = matrix[mid // c][mid % c]
            if target == x:
                return True
            elif x > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

