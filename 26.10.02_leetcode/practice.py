# 2026.10.02力扣网刷题
# 357. 统计各位数字都不同的数字个数——数学、动态规划、回溯——中等
# 给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
# 示例 1：
# 输入：n = 2
# 输出：91
# 解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。
# 示例 2：
# 输入：n = 0
# 输出：1
# 提示：
# 0 <= n <= 8

class Solution:
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
        dp = [0] * 9
        dp[0] = 1
        dp[1] = 9
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)
        ans = 0
        for i in range(0, n + 1):
            ans += dp[i]
        return ans

    def dfs(self, n, visited, level):
        if level > n:
            return
        self.ans += 1
        if level == n:
            return
        
        for i in range(10):
            if visited[i] == False:
                visited[i] = True
                self.dfs(n, visited, level + 1)
                visited[i] = False
                
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        self.ans = 1
        visited = [False] * 10
        for i in range(1, 10):
            visited[i] = True
            self.dfs(n, visited, 1)
            visited[i] = False
        return self.ans