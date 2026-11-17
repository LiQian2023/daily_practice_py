# 2026.11.17力扣网刷题
# LCR 082. 组合总和 II——数组、回溯——中等
# 给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。
# 示例 1：
# 输入：candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
# 输出：
# [
# 	[1, 1, 6],
# 	[1, 2, 5],
# 	[1, 7],
# 	[2, 6]
# ]
# 示例 2：
# 输入：candidates = [2, 5, 2, 1, 2], target = 5
# 输出：
# [
# 	[1, 2, 2],
# 	[5]
# ]
# 提示：
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
# 注意：本题与主站 40 题相同： https ://leetcode.cn/problems/combination-sum-ii/

from typing import List

class Solution:
    def backTrack(self, nums, target, ans, stack, begin, total):
        if total == target:
            ans.append(stack)
            return
        for i in range(begin, len(nums)):
            if i > begin and nums[i] == nums[i - 1]:
                continue
            if total + nums[i] > target:
                break
            self.backTrack(nums, target, ans, stack + [nums[i]], i + 1, total + nums[i])
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.backTrack(candidates, target, ans, [], 0, 0)
        return ans