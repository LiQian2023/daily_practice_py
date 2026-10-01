# 2026.10.01力扣网刷题
# 494. 目标和——数组、动态规划、回溯、背包问题、0-1背包——中等
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
# 示例 1：
# 输入：nums = [1, 1, 1, 1, 1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# - 1 + 1 + 1 + 1 + 1 = 3
# + 1 - 1 + 1 + 1 + 1 = 3
# + 1 + 1 - 1 + 1 + 1 = 3
# + 1 + 1 + 1 - 1 + 1 = 3
# + 1 + 1 + 1 + 1 - 1 = 3
# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1
# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# - 1000 <= target <= 1000

class Solution:
    def dfs(self, nums, target, state, dp):
        if state[0] == len(nums):
            return 1 if state[1] == target else 0
        if state not in dp:
            state1 = (state[0] + 1, state[1] + nums[state[0]])
            state2 = (state[0] + 1, state[1] - nums[state[0]])
            dp[state] = self.dfs(nums, target, state1, dp) + self.dfs(nums, target, state2, dp)
        return dp[state]
        
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}
        return self.dfs(nums, target, (0, 0), dp)