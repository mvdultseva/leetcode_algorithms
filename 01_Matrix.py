"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.

"""
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for k in range(n):
                if matrix[i][k] != 0:
                    matrix[i][k] = float("inf")
                    if i > 0 and matrix[i-1][k] + 1 < matrix[i][k]:
                        matrix[i][k] = matrix[i - 1][k] + 1
                    if k > 0 and matrix[i][k - 1] + 1 < matrix[i][k]:
                        matrix[i][k] = matrix[i][k - 1] + 1
        for i in range(m - 1, -1, -1):
            for k in range(n - 1, -1, -1):
                if matrix[i][k] !=0:
                    if i + 1 < m and matrix[i + 1][k] + 1 < matrix[i][k]:
                        matrix[i][k] = matrix[i + 1][k] + 1
                    if k + 1 < n and matrix[i][k + 1] + 1 < matrix[i][k]:
                        matrix[i][k] = matrix[i][k + 1] + 1
        return matrix