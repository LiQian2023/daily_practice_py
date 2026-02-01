# 2026.02.02力扣网刷题
# 面试题 16.17.连续数列——数组、分治、动态规划——简单
# 给定一个整数数组，找出总和最大的连续数列，并返回总和。
# 示例：
# 输入：[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出： 6
# 解释： 连续子数组[4, -1, 2, 1] 的和最大，为 6。
# 进阶：
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp, ans = nums[0], nums[0]
        for num in nums[1::]:
            dp = max(num, dp + num)
            ans = max(ans, dp)
        return ans