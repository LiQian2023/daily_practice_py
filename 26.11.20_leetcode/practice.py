# 2026.11.20力扣网刷题
# LCR 083. 全排列——数组、回溯——中等
# 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。
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
# 注意：本题与主站 46 题相同：https://leetcode.cn/problems/permutations/

from typing import List

class Solution:
    def backTrack(self, nums, stack, ans, visited, top):
        if top == len(nums):
            ans.append(stack[::])
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            stack.append(nums[i])
            self.backTrack(nums, stack, ans, visited, top + 1)
            visited[i] = False
            stack.pop()
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, stack, visited = [], [], [False] * len(nums)
        self.backTrack(nums, stack, ans, visited, 0)
        return ans