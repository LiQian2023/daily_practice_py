# 2025.12.13力扣网刷题
# 2765. 最长交替子数组——数组、枚举、第108场双周赛——简单
# 给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：
# m 大于 1 。
# s1 = s0 + 1 。
# 下标从 0 开始的子数组 s 与数组[s0, s1, s0, s1, ..., s(m - 1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
# 请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 - 1 。
# 子数组是一个数组中一段连续 非空 的元素序列。
# 示例 1：
# 输入：nums = [2, 3, 4, 3, 4]
# 输出：4
# 解释：交替子数组有[2, 3]，[3, 4]，[3, 4, 3] 和[3, 4, 3, 4]。最长的子数组为[3, 4, 3, 4]，长度为 4。
# 示例 2：
# 输入：nums = [4, 5, 6]
# 输出：2
# 解释：[4, 5] 和[5, 6] 是仅有的两个交替子数组。它们长度都为 2 。
# 提示：
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10^4

class Solution(object):
    def alternatingSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r, ans = 0, 1, 0
        length, flag = len(nums), 1
        while l < length - 1 and nums[l + 1] - nums[l] != 1:
            l += 1
        r = l + 1
        flag = 0
        while r < length:
            if nums[r] - nums[r - 1] != 1 and nums[r] - nums[r - 1] != -1:
                if r - l > ans:
                    ans = r - l
                l = r
                flag = 1
            elif r + 1 < length and nums[r + 1] != nums[r - 1]:
                if r + 1 - l > ans:
                    ans = r + 1 - l
                l = r
                flag = 1
            if flag == 1:
                while l < length - 1 and nums[l + 1] - nums[l] != 1:
                    l += 1
                r = l
                flag = 0
            r += 1
        if r - l > ans:
            ans = r - l
        return ans if ans > 1 else -1



