class Solution(object):
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True

sol = Solution()

matrix1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix2 = [[1,2],[2,2]]

print(sol.isToeplitzMatrix(matrix1))
print(sol.isToeplitzMatrix(matrix2))
