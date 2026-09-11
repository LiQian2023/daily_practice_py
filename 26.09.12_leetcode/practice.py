# 2026.09.12力扣网刷题
# 46. 全排列——数组、回溯——中等
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出： [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# 示例 2：
# 输入：nums = [0, 1]
# 输出： [[0, 1], [1, 0]]
# 示例 3：
# 输入：nums = [1]
# 输出： [[1]]
# 提示：
# 1 <= nums.length <= 6
# - 10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
from typing import List
class Solution:
    def dfs(self, nums, stack, visited, ans):
        if len(stack) == len(nums):
            ans.append(stack)
            return
        for i in range(len(nums)):
            if visited[i] == False:
                visited[i] = True
                self.dfs(nums, stack + [nums[i]], visited, ans)
                visited[i] = False
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack, visited, ans = [], [False] * len(nums), []
        self.dfs(nums, stack, visited, ans)
        return ans