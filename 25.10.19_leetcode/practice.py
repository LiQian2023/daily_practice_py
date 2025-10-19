# 2025.10.19力扣网刷题
# 二进制矩阵中的特殊位置——数组、矩阵、第206场周赛——简单
# 给定一个 m x n 的二进制矩阵 mat，返回矩阵 mat 中特殊位置的数量。
# 如果位置(i, j) 满足 mat[i][j] == 1 并且行 i 与列 j 中的所有其他元素都是 0（行和列的下标从 0 开始计数），那么它被称为 特殊 位置。
# 示例 1：
# 输入：mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
# 输出：1
# 解释：位置(1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
# 示例 2：
# 输入：mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# 输出：3
# 解释：位置(0, 0)，(1, 1) 和(2, 2) 都是特殊位置。
# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# mat[i][j] 是 0 或 1。

class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        row, col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                row[i] += mat[i][j]
                col[j] += mat[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
                    ans += 1
        return ans