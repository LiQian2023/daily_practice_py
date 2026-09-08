# 2026.09.08力扣网刷题
# 40. 组合总和 II——数组、回溯——中等
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用 一次 。
# 注意：解集不能包含重复的组合。
# 示例 1:
# 输入: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8,
# 输出 :
# [
# 	[1, 1, 6],
# 	[1, 2, 5],
# 	[1, 7],
# 	[2, 6]
# ]
# 示例 2:
# 输入: candidates = [2, 5, 2, 1, 2], target = 5,
# 输出 :
# [
# 	[1, 2, 2],
# 	[5]
# ]
# 提示 :
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
from typing import List
class Solution:
    def DFS(self, nums, stack, ans, curren_sum, start, target):
        if curren_sum == target:
            ans.append(stack)
            return
        for i in range(start, len(nums)):
            if curren_sum + nums[i] > target:
                break
            if i > start and nums[i] == nums[i-1]:
                continue
            self.DFS(nums, stack + [nums[i]], ans, curren_sum + nums[i], i + 1, target)
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, stack = [], []
        candidates.sort()
        self.DFS(candidates, stack, ans, 0, 0, target)
        return ans