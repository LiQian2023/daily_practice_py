# 2025.04.15力扣网刷题
# 数组的度——数组、哈希表——简单
# 给定一个非空且只包含非负数的整数数组 nums，数组的 度 的定义是指数组里任一元素出现频数的最大值。
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
# 示例 1：
# 输入：nums = [1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
# 连续子数组里面拥有相同度的有如下所示：
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2] 的长度为 2 ，所以返回 2 。
# 示例 2：
# 输入：nums = [1, 2, 2, 3, 1, 4, 2]
# 输出：6
# 解释：
# 数组的度是 3 ，因为元素 2 重复出现 3 次。
# 所以[2, 2, 3, 1, 4, 2] 是最短子数组，因此返回 6 。
# 提示：
# nums.length 在 1 到 50, 000 范围内。
# nums[i] 是一个在 0 到 49, 999 范围内的整数。

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_list = list(set(nums))
        my_dict = dict(zip(my_list, [nums.count(num) for num in my_list]))
        len1 = len(nums)
        max_num = max(my_dict.values())
        pi_dict = {}
        for i in range(len1):
            if nums[i] in pi_dict:
                pi_dict[nums[i]][1] = i
            else:
                pi_dict[nums[i]] = [i, 0]
        ans = 0
        for key in my_dict:
            if my_dict[key] == max_num:
                tmp = pi_dict[key][1] - pi_dict[key][0] + 1
                if tmp > 0:
                    if ans == 0 or tmp < ans:
                        ans = tmp
        return ans
