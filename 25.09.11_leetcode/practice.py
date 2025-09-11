# 2025.09.11力扣网刷题
# 分割等和子集——数学、字符串、模拟——简单
# 给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。
# 示例 1：
# 输入：nums = [1, 5, 11, 5]
# 输出：true
# 解释：nums 可以分割成[1, 5, 5] 和[11] 。
# 示例 2：
# 输入：nums = [1, 2, 3, 5]
# 输出：false
# 解释：nums 不可以分为和相等的两部分
# 提示：
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
# 注意：本题与主站 416 题相同： https ://leetcode-cn.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False

        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False

        target = total // 2
        if maxNum > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n - 1][target]

