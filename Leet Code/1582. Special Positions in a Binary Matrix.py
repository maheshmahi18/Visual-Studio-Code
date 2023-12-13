"""

1582. Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:

Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.


Example 2:

Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.


Solution: Done in Python

"""

class Solution(object):
    def numSpecial(self, mat):
        c = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                     if self.check(mat, i, j)==(1,1): c+=1
        return c

    def check(self, mat, i, j):
        a = mat[i]
        b = [mat[k][j] for k in range(len(mat))]
        c=a.count(1)
        d=b.count(1)
        return c,d
    
s=Solution()
n=eval(input())
print(s.numSpecial(n))