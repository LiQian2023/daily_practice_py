# 2024.09.21力扣网刷题
# 最接近的三数之和——数组、双指针、排序——中等
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在恰好一个解。
# 示例 1：
# 输入：nums = [-1, 2, 1, -4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
# 示例 2：
# 输入：nums = [0, 0, 0], target = 1
# 输出：0
# 解释：与 target 最接近的和是 0（0 + 0 + 0 = 0）。
# 提示：
# 3 <= nums.length <= 1000
# - 1000 <= nums[i] <= 1000
# - 10^4 <= target <= 10^4


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 方法一：双指针
        nums.sort()
        min = target - sum(nums[:3])
        length = len(nums)
        for i in range(length):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(min) > abs(target - tmp):
                    min = target - tmp
                if tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    break
        return target - min
