# 2026.10.28力扣网刷题
# 3882. 网格图中最小异或路径——资深工程师、位运算、数组、动态规划、矩阵、第179场双周赛——中等
# 给你一个大小为 m * n 的二维整数数组 grid。
# 你从 左上角 的单元格(0, 0) 出发，想要到达 右下角 的单元格(m - 1, n - 1)。
# 在每一步中，你 可以 向右或向下 移动。
# 路径的 代价 定义为该路径上所有单元格（包括 起点和终点）的值的 按位异或。
# 返回从(0, 0) 到(m - 1, n - 1) 的所有有效路径中 最小 的可能异或值。
# 示例 1：
# 输入： grid = [[1, 2], [3, 4]]
# 输出： 6
# 解释：
# 有两条有效路径：
# (0, 0) →(0, 1) →(1, 1)，异或值为：1 XOR 2 XOR 4 = 7
# (0, 0) →(1, 0) →(1, 1)，异或值为：1 XOR 3 XOR 4 = 6
# 所有有效路径中的最小异或值为 6。
# 示例 2：
# 输入： grid = [[6, 7], [5, 8]]
# 输出： 9
# 解释：
# 有两条有效路径：
# (0, 0) →(0, 1) →(1, 1)，异或值为：6 XOR 7 XOR 8 = 9
# (0, 0) →(1, 0) →(1, 1)，异或值为：6 XOR 5 XOR 8 = 11
# 所有有效路径中的最小异或值为 9。
# 示例 3：
# 输入： grid = [[2, 7, 5]]
# 输出： 0
# 解释：
# 只有一条有效路径：
# (0, 0) →(0, 1) →(0, 2)，异或值为：2 XOR 7 XOR 5 = 0
# 这条路径的异或值为 0，这是可能达到的最小值。
# 提示：
# 1 <= m == grid.length <= 1000
# 1 <= n == grid[i].length <= 1000
# m * n <= 1000
# 0 <= grid[i][j] <= 1023

class Solution:
    def dfs(self, grid, m, n, visited, x, y, val):
        if x >= m or y >= n:
            return
        val ^= grid[x][y]
        if visited[x][y][val]:
            return
        visited[x][y][val] = 1
        if x == m - 1 and y == n - 1:
            return
        self.dfs(grid, m, n, visited, x + 1, y, val)
        self.dfs(grid, m, n, visited, x, y + 1, val)
        
    def minCost1(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[[False] * 1024 for _ in range(n)] for _ in range(m)]
        self.dfs(grid, m, n, visited, 0, 0, 0)
        ans = 0
        for i in range(1024):
            if visited[m - 1][n - 1][i]:
                ans = i
                break
        return ans
    
    def minCost2(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[False] * 1024 for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                for k in range(1024):
                    if not dp[i][j][k]:
                        continue
                    if i < m -1:
                        dp[i + 1][j][k ^ grid[i + 1][j]] = True
                    if j < n - 1:
                        dp[i][j + 1][k ^ grid[i][j + 1]] = True
        ans = 0
        for i in range(1024):
            if dp[m - 1][n - 1][i]:
                ans = i
                break
        return ans
    
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[False] * 1024 for _ in range(n)]
        dp[0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cur = [False] * 1024
                for k in range(1024):
                    if (i > 0 and dp[j][k]) or (j > 0 and dp[j - 1][k]):
                        cur[k ^ grid[i][j]] = True
                dp[j] = cur
        ans = 0
        for i in range(1024):
            if dp[n - 1][i]:
                ans = i
                break
        return ans