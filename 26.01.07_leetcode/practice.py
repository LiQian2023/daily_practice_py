# 2026.01.07力扣网刷题
# 3736. 最小操作次数使数组元素相等 III——数组、数学、第169场双周赛——简单
# 给你一个整数数组 nums。
# 在一步操作中，你可以将任意单个元素 nums[i] 的值 增加 1。
# 返回使数组中的所有元素都 相等 所需的 最小总操作次数 。
# 示例 1:
# 输入: nums = [2, 1, 3]
# 输出 : 3
# 解释 :
# 使所有元素相等的操作如下 :
# 将 nums[0] = 2 增加 1, 变为 3。
# 将 nums[1] = 1 增加 1, 变为 2。
# 将 nums[1] = 2 增加 1, 变为 3。
# 现在，nums 中的所有元素都等于 3。最小总操作次数为 3。
# 示例 2:
# 输入: nums = [4, 4, 5]
# 输出 : 2
# 解释 :
# 使所有元素相等的操作如下 :
# 将 nums[0] = 4 增加 1, 变为 5。
# 将 nums[1] = 4 增加 1, 变为 5。
# 现在，nums 中的所有元素都等于 5。最小总操作次数为 2。
# 提示:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


class Solution(object):
    def minMoves1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num, ans, tmp = nums[0], 0, 0
        for i in range(len(nums)):
            tmp += nums[i]
            if nums[i] > max_num:
                max_num = nums[i]
            if max_num * (i + 1) > tmp:
                ans = max_num * (i + 1) - tmp
        return ans

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums) * len(nums) - sum(nums)