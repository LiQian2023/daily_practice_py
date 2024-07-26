# 2024.07.26力扣网刷题
# 有序数组的平方——数组、双指针、排序——简单
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
# 示例 1：
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 解释：平方后，数组变为[16, 1, 0, 9, 100]
# 排序后，数组变为[0, 1, 9, 16, 100]
# 示例 2：
# 输入：nums = [-7, -3, 2, 3, 11]
# 输出：[4, 9, 9, 49, 121]
# 提示：
# 1 <= nums.length <= 10^4
# - 10^4 <= nums[i] <= 10^4
# nums 已按 非递减顺序 排序
# 进阶：
# 请你设计时间复杂度为 O(n) 的算法解决本问题

class Solution(object):
    def sortedSquares1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        l, r = 0, len(nums) - 1
        i = r
        while l <= r:
            x = nums[l]**2
            y = nums[r]**2
            if x > y:
                max = x
                l += 1
            else:
                max = y
                r -= 1
            ans[i] = max
            i -= 1
        return ans


    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums
