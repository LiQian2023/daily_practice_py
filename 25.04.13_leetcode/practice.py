# 2025.04.13力扣网刷题
# 在长度 2N 的数组中找出重复 N 次的元素——数组、哈希表——简单
# 给你一个整数数组 nums ，该数组具有以下属性：
# nums.length == 2 * n.
# nums 包含 n + 1 个 不同的 元素
# nums 中恰有一个元素重复 n 次
# 找出并返回重复了 n 次的那个元素。
# 示例 1：
# 输入：nums = [1, 2, 3, 3]
# 输出：3
# 示例 2：
# 输入：nums = [2, 1, 2, 5, 3, 2]
# 输出：2
# 示例 3：
# 输入：nums = [5, 1, 5, 2, 5, 3, 5, 4]
# 输出：5
# 提示：
# 2 <= n <= 5000
# nums.length == 2 * n
# 0 <= nums[i] <= 10^4
# nums 由 n + 1 个 不同的 元素组成，且其中一个元素恰好重复 n 次

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, min_num = nums[0], nums[0]
        length = len(nums)
        for i in range(length):
            if nums[i] < min_num:
                min_num = nums[i]
            elif nums[i] > max_num:
                max_num = nums[i]
        size = max_num - min_num + 1
        hash = [0] * size
        ans = 0
        for num in nums:
            key = num - min_num
            hash[key] += 1
            if hash[key] >= length // 2:
                ans = num
                break
        return ans