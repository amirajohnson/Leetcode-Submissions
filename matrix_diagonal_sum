'''
Prompt: 
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        #have i working forwards and j working backwards
        i, j = 0, len(mat)-1
        total = 0

        #i (rows) increases by one on each iteration, j (cols) decreases by one on each iteration
        while (i < len(mat) and j >= 0): # will work if the matrix is square
            total += mat[i][j]
            total += mat[i][i]
            print((i,j), (i,i))
            i+=1
            j-=1
    
        #subtract the middle which was double counted (only in the case that the dimensions are odd)
        if len(mat) % 2 != 0:
            total -= mat[len(mat)/2][len(mat)/2]
        return total
