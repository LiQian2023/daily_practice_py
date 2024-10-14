# 2024.10.14力扣网刷题
# 排序数组——数组、分治、桶排序、计数排序、基数排序、排序、堆（优先队列）、归并排序——中等
# 给你一个整数数组 nums，请你将该数组升序排列。
# 你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。
# 示例 1：
# 输入：nums = [5, 2, 3, 1]
# 输出：[1, 2, 3, 5]
# 示例 2：
# 输入：nums = [5, 1, 1, 2, 0, 0]
# 输出：[0, 0, 1, 1, 2, 5]
# 提示：
# 1 <= nums.length <= 5 * 10^4
# - 5 * 10^4 <= nums[i] <= 5 * 10^4

class Solution(object):
    def Adjust_Down(self, nums, size, parent):
        child = parent * 2 + 1
        while child < size:
            if child + 1 < size and nums[child] <= nums[child + 1]:
                child = child + 1
            if nums[parent] <= nums[child]:
                nums[parent], nums[child] = nums[child], nums[parent]
            parent = child
            child = parent * 2 + 1

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 堆排序
        length = len(nums)
        # 建堆
        for i in range((length - 1) // 2, -1, -1):
            Solution().Adjust_Down(nums, length, i)
        # 排序
        for i in range(length - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            Solution().Adjust_Down(nums, i, 0)
        return nums
