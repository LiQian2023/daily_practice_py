# 2024.09.24力扣网刷题
# 四数之和——数组、双指针、排序——中等
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
# 请你找出并返回满足下述全部条件且不重复的四元组[nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
# 示例 1：
# 输入：nums = [1, 0, -1, 0, -2, 2], target = 0
# 输出： [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# 示例 2：
# 输入：nums = [2, 2, 2, 2, 2], target = 8
# 输出： [[2, 2, 2, 2]]
# 提示：
# 1 <= nums.length <= 200
# - 10^9 <= nums[i] <= 10^9
# - 10^9 <= target <= 10^9


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 方法一：排序+双指针
        nums.sort()
        length = len(nums)
        ans = []
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, length):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, length - 1
                while l < r:
                    if nums[l] + nums[r] > target - nums[i] - nums[j]:
                        r -= 1
                    elif nums[l] + nums[r] < target - nums[i] - nums[j]:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return ans