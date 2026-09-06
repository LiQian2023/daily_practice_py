# 2026.09.06力扣网刷题
# 22. 括号生成——字符串、动态规划、回溯、括号序列——中等
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 示例 1：
# 输入：n = 3
# 输出：["((()))", "(()())", "(())()", "()(())", "()()()"]
# 示例 2：
# 输入：n = 1
# 输出：["()"]
# 提示：
# 1 <= n <= 8
from typing import List
class Solution:
    def DFS(self, stack, n, ans, left, right):
        if len(stack) == 2 * n:
            ans.append(''.join(stack))
            return
        if left < n:
            stack.append('(')
            self.DFS(stack, n, ans, left + 1, right)
            stack.pop()
        if right < left:
            stack.append(')')
            self.DFS(stack, n, ans, left, right + 1)
            stack.pop()
            
    def generateParenthesis(self, n: int) -> List[str]:
        stack, ans = [], []
        left, right = 0, 0
        self.DFS(stack, n, ans, left, right)
        return ans