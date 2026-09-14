# 2026.09.14力扣网刷题
# 77. 组合——回溯——中等
# 给定两个整数 n 和 k，返回范围[1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
# 示例 1：
# 输入：n = 4, k = 2
# 输出：
# [
# 	[2, 4],
# 	[3, 4],
# 	[2, 3],
# 	[1, 2],
# 	[1, 3],
# 	[1, 4],
# ]
# 示例 2：
# 输入：n = 1, k = 1
# 输出： [[1]]
# 提示：
# 1 <= n <= 20
# 1 <= k <= n
from typing import List
class Solution:
    def dfs(self, n, k, stack, visited, res, start):
        if len(stack) == k:
            res.append(stack[::])
            return
        for i in range(start, n + 1):
            if visited[i]:
                continue
            visited[i] = True
            self.dfs(n, k, stack + [i], visited,res, i + 1)
            visited[i] = False
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack, visited, res = [], [False] * (n + 1), []
        self.dfs(n, k, stack, visited, res, 1)
        return res