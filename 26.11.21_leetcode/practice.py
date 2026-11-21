# 2026.11.21力扣网刷题
# LCR 084. 全排列 II——数组、回溯——中等
# 给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。
# 示例 1：
# 输入：nums = [1, 1, 2]
# 输出：
# [[1, 1, 2],
# [1, 2, 1],
# [2, 1, 1]]
# 示例 2：
# 输入：nums = [1, 2, 3]
# 输出： [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# 提示：
# 1 <= nums.length <= 8
# - 10 <= nums[i] <= 10
# 注意：本题与主站 47 题相同： https ://leetcode.cn/problems/permutations-ii/

from typing import List
class Solution:
    def backTrack(self, nums, stack, visited, ans):
        if len(stack) == len(nums):
            ans.append(stack[::])
            return
        for i in range(len(nums)):
            if visited[i] or (i > 0 and nums[i - 1] == nums[i] and visited[i - 1] == False):
                continue
            visited[i] = True
            stack.append(nums[i])
            self.backTrack(nums, stack, visited, ans)
            stack.pop()
            visited[i] = False
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, stack, visited = [], [], [False] * len(nums)
        self.backTrack(nums, stack, visited, ans)
        return ans
