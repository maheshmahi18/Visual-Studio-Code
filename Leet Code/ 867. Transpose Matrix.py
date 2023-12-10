"""

867. Transpose Matrix


Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]


Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-10^9 <= matrix[i][j] <= 10^9


Solution: Done in Python

"""

class Solution(object):
  def transpose(self,matrix):
    a=[]
    for i in range(len(matrix[0])):
      b=[]
      for j in range(len(matrix)):
        b.append(matrix[j][i])
      a.append(b)
    return a
    

sol = Solution()
example_matrix = eval(input())
print(sol.transpose(example_matrix))