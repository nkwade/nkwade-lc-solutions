class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        
        if l == r and matrix[0][0] == target:
            return True
        while l < r:
            m = (l + r) // 2
            if matrix[m // len(matrix[0])][m % len(matrix[0])] == target:
                return True
            if matrix[m // len(matrix[0])][m % len(matrix[0])] > target:
                r = m
            else:
                l = m + 1
        return matrix[l // len(matrix[0])][l % len(matrix[0])] == target