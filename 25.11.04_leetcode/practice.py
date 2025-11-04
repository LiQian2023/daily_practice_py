# 2025.11.04力扣网刷题
# 判断矩阵经轮转后是否一致——数组、矩阵、第244场周赛——简单
# 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：mat = [[0, 1], [1, 0]], target = [[1, 0], [0, 1]]
# 输出：true
# 解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
# 示例 2：
# 输入：mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
# 输出：false
# 解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
# 示例 3：
# 输入：mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
# 输出：true
# 解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
# 提示：
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] 和 target[i][j] 不是 0 就是 1

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def Rotation(mat, n, k):
            up, right, down, left = [], [], [], []
            for i in range(k, n - k):
                up.append(mat[k][i])
                down.append(mat[n - k - 1][i])
                right.insert(0, mat[i][n - k - 1])
                left.insert(0, mat[i][k])
            pi = 0
            for i in range(k, n - k):
                mat[k][i] = left[pi]
                mat[n - k][i] = right[pi]
                mat[i][n - k - 1] = up[pi]
                mat[i][k] = down[pi]
                pi += 1

        n = len(mat)
        for i in range(4):
            for k in range(n):
                if (k == n - k - 1):
                    break
                Rotation(mat, n, k)
            if mat == target:
                return True
        return False

