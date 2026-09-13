# 2026.09.13力扣网刷题
# 47. 全排列 II——数组、回溯、排序——中等
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
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
from typing import List
class Solution:
    def dfs(self, nums, stack, visited, ans):
        if(len(stack) == len(nums)):
            ans.append(stack)
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True
            self.dfs(nums, stack+[nums[i]], visited, ans)
            visited[i] = False
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack, visited, ans = [], [False] * len(nums), []
        self.dfs(nums, stack, visited, ans)
        return ans