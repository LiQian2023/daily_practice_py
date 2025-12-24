# 2025.12.24力扣网刷题
# 3095. 或值至少 K 的最短子数组 I——位运算、数组、滑动窗口、第127场双周赛——简单
# 给你一个 非负 整数数组 nums 和一个整数 k 。
# 如果一个数组中所有元素的按位或运算 OR 的值 至少 为 k ，那么我们称这个数组是 特别的 。
# 请你返回 nums 中 最短特别非空 子数组的长度，如果特别子数组不存在，那么返回 - 1 。
# 示例 1：
# 输入：nums = [1, 2, 3], k = 2
# 输出：1
# 解释：
# 子数组[3] 的按位 OR 值为 3 ，所以我们返回 1 。
# 注意，[2] 也是一个特别子数组。
# 示例 2：
# 输入：nums = [2, 1, 8], k = 10
# 输出：3
# 解释：
# 子数组[2, 1, 8] 的按位 OR 值为 11 ，所以我们返回 3 。
# 示例 3：
# 输入：nums = [1, 2], k = 0
# 输出：1
# 解释：
# 子数组[1] 的按位 OR 值为 1 ，所以我们返回 1 。
# 提示：
# 1 <= nums.length <= 50
# 0 <= nums[i] <= 50
# 0 <= k < 64

class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = -1
        for gap in range(1, len(nums) + 1):
            for l in range(len(nums)):
                tmp = 0
                for r in range(l, l + gap):
                    if r == len(nums):
                        break
                    tmp = tmp | nums[r]
                if tmp >= k:
                    ans = gap
                    break
            if ans != -1:
                break
        return ans