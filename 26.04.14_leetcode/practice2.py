# 2024.03.24力扣网刷题
# 2026.04.14完成解答并通过力扣所有测试用例
# 零钱兑换——广度优先搜索、数组、动态规划——中等
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 - 1 。
# 你可以认为每种硬币的数量是无限的。
# 示例 1：
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
# 示例 2：
# 输入：coins = [2], amount = 3
# 输出： - 1
# 示例 3：
# 输入：coins = [1], amount = 0
# 输出：0
# 提示：
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        dp = [INT_MAX] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                tmp = i - coin
                dp[i] = dp[i] if tmp < 0 else min(dp[i], dp[tmp] + 1)
        return dp[amount] if dp[amount] != INT_MAX else -1