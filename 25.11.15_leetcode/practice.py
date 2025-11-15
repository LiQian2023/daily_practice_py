# 2025.11.15力扣网刷题
# 2373. 矩阵中的局部最大值——数组、矩阵、第306场周赛——简单
# 给你一个大小为 n x n 的整数矩阵 grid 。
# 生成一个大小为(n - 2) x(n - 2) 的整数矩阵  maxLocal ，并满足：
# maxLocal[i][j] 等于 grid 中以 i + 1 行和 j + 1 列为中心的 3 x 3 矩阵中的 最大值 。
# 换句话说，我们希望找出 grid 中每个 3 x 3 矩阵中的最大值。
# 返回生成的矩阵。
# 示例 1：
# 输入：grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
# 输出： [[9, 9], [8, 6]]
# 解释：原矩阵和生成的矩阵如上图所示。
# 注意，生成的矩阵中，每个值都对应 grid 中一个相接的 3 x 3 矩阵的最大值。
# 示例 2：
# 输入：grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
# 输出： [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
# 解释：注意，2 包含在 grid 中每个 3 x 3 的矩阵中。
# 提示：
# n == grid.length == grid[i].length
# 3 <= n <= 100
# 1 <= grid[i][j] <= 100

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(grid)
        row = 0
        coordinates = []
        for i in range(n):
            if i + 1 < n - 1:
                row += 1
                ans.append([])
                for j in range(n):
                    if j + 1 < n - 1:
                        coordinates.append([i + 1, j + 1])

        def Get_Max(coordinates, row, col):
            num = grid[row][col]
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    tmp = grid[row + i][col + j]
                    if tmp > num:
                        num = tmp
            return num


        i = 0
        for j in range(row):
            for z in range(row):
                r, c = coordinates[i][0], coordinates[i][1]
                ans[j].append(Get_Max(coordinates, r, c))
                i += 1
        return ans
