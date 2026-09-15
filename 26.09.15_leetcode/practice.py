# 2026.09.15力扣网刷题
# 78. 子集——位运算、数组、回溯——中等
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出： [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# 示例 2：
# 输入：nums = [0]
# 输出： [[], [0]]
# 提示：
# 1 <= nums.length <= 10
# - 10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
from typing import List
class Solution:
    def dfs(self, nums, stack, ans, start):
        ans.append(stack)
        for i in range(start, len(nums)):
            self.dfs(nums, stack+[nums[i]], ans, i + 1)
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack, ans = [], []
        self.dfs(nums, stack, ans, 0)
        return ans