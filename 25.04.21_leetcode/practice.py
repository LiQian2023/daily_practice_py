# 2025.04.21力扣网刷题
# 检查是否每一行每一列都包含全部整数——数组、哈希表、矩阵——简单
# 对一个大小为 n x n 的矩阵而言，如果其每一行和每一列都包含从 1 到 n 的 全部 整数（含 1 和 n），则认为该矩阵是一个 有效 矩阵。
# 给你一个大小为 n x n 的整数矩阵 matrix ，请你判断矩阵是否为一个有效矩阵：如果是，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
# 输出：true
# 解释：在此例中，n = 3 ，每一行和每一列都包含数字 1、2、3 。
# 因此，返回 true 。
# 示例 2：
# 输入：matrix = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
# 输出：false
# 解释：在此例中，n = 3 ，但第一行和第一列不包含数字 2 和 3 。
# 因此，返回 false 。
# 提示：
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# 1 <= matrix[i][j] <= n

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            Row = [0] * 101
            Col = [0] * 101
            for j in range(n):
                key1, key2 = matrix[i][j], matrix[j][i]
                if Row[key1] or Col[key2]:
                    return False
                Row[key1] = 1
                Col[key2] = 1
        return True

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    print(s.checkValid(matrix))