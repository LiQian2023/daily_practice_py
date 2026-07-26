# 2026.07.26力扣网刷题
# 628. 三个数的最大乘积——数组、数学、排序——简单
# 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：6
# 示例 2：
# 输入：nums = [1, 2, 3, 4]
# 输出：24
# 示例 3：
# 输入：nums = [-1, -2, -3]
# 输出： - 6
# 提示：
# 3 <= nums.length <= 10^4
# - 1000 <= nums[i] <= 1000
from typing import List
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        heap1 = [-1001, -1001, -1001]
        heap2 = [1001, 1001, 1001]
        for i in range(len(nums)):
            if nums[i] > heap1[0]:
                heap1[2] = heap1[1]
                heap1[1] = heap1[0]
                heap1[0] = nums[i]
            elif nums[i] > heap1[1]:
                heap1[2] = heap1[1]
                heap1[1] = nums[i]
            elif nums[i] > heap1[2]:
                heap1[2] = nums[i]
            if nums[i] < heap2[0]:
                heap2[2] = heap2[1]
                heap2[1] = heap2[0]
                heap2[0] = nums[i]
            elif nums[i] < heap2[1]:
                heap2[2] = heap2[1]
                heap2[1] = nums[i]
            elif nums[i] < heap2[2]:
                heap2[2] = nums[i]
        ans1, ans2 = heap1[0] * heap1[1] * heap1[2], heap2[0] * heap2[1] * heap1[0]
        return max(ans1, ans2)
        