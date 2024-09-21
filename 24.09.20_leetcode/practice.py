# 2024.09.20力扣网刷题
# 三数之和——数组、双指针、排序——中等
# 给你一个整数数组 nums ，判断是否存在三元组[nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出： [[-1, -1, 2], [-1, 0, 1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是[-1, 0, 1] 和[-1, -1, 2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
# 输入：nums = [0, 1, 1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
# 输入：nums = [0, 0, 0]
# 输出： [[0, 0, 0]]
# 解释：唯一可能的三元组和为 0 。
# 提示：
# 3 <= nums.length <= 3000
# - 10^5 <= nums[i] <= 10^5


class Solution(object):
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 方法一：双指针
        nums.sort()
        length = len(nums)
        ans = []
        for i in range(length):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while 0 <= l < r < length:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return ans


nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
print(Solution.threeSum(nums))
