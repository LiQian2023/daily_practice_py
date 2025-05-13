# 2025.05.13力扣网刷题
# 删除后的最大子数组元素和——贪心、数组、哈希表——简单
# 给你一个整数数组 nums 。
# 你可以从数组 nums 中删除任意数量的元素，但不能将其变为 空 数组。执行删除操作后，选出 nums 中满足下述条件的一个子数组：
# 子数组中的所有元素 互不相同 。
# 最大化 子数组的元素和。
# 返回子数组的 最大元素和 。
# 子数组 是数组的一个连续、非空 的元素序列。
# 示例 1：
# 输入：nums = [1, 2, 3, 4, 5]
# 输出：15
# 解释：
# 不删除任何元素，选中整个数组得到最大元素和。
# 示例 2：
# 输入：nums = [1, 1, 0, 1, 1]
# 输出：1
# 解释：
# 删除元素 nums[0] == 1、nums[1] == 1、nums[2] == 0 和 nums[3] == 1 。选中整个数组[1] 得到最大元素和。
# 示例 3：
# 输入：nums = [1, 2, -1, -2, 1, 0, -1]
# 输出：3
# 解释：
# 删除元素 nums[2] == -1 和 nums[3] == -2 ，从[1, 2, 1, 0, -1] 中选中子数组[2, 1] 以获得最大元素和。
# 提示：
# 1 <= nums.length <= 100
# - 100 <= nums[i] <= 100

class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = nums[0], nums[0]
        for num in nums:
            begin = min(begin, num)
            end = max(end, num)
        size = end - begin + 1
        hash = [0] * size
        for num in nums:
            key = num - begin
            hash[key] += 1
        ans, tmp = 0, 0
        for i in range(size - 1, -1, -1):
            if i + begin == 0:
                break
            if hash[i]:
                tmp += i + begin
            if ans == 0 or tmp > ans:
                ans = tmp
        return ans