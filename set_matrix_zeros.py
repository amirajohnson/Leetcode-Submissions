'''
Prompt:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_rows = []
        zero_cols = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.append(row)
                    zero_cols.append(col)

        for r in zero_rows:
            matrix[r] = [0 for i in range(len(matrix[0]))]
        for c in zero_cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0
