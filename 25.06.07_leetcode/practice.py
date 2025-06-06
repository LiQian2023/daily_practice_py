# 2025.06.07力扣网刷题
# 数位和等于下标的最小下标——数组、数学——简单
# 给你一个整数数组 nums 。
# 返回满足 nums[i] 的数位和（每一位数字相加求和）等于 i 的 最小 下标 i 。
# 如果不存在满足要求的下标，返回 - 1 。
# 示例 1：
# 输入：nums = [1, 3, 2]
# 输出：2
# 解释：
# nums[2] = 2，其数位和等于 2 ，与其下标 i = 2 相等。因此，输出为 2 。
# 示例 2：
# 输入：nums = [1, 10, 11]
# 输出：1
# 解释：
# nums[1] = 10，其数位和等于 1 + 0 = 1，与其下标 i = 1 相等。
# nums[2] = 11，其数位和等于是 1 + 1 = 2，与其下标 i = 2 相等。
# 由于下标 1 是满足要求的最小下标，输出为 1 。
# 示例 3：
# 输入：nums = [1, 2, 3]
# 输出： - 1
# 解释：
# 由于不存在满足要求的下标，输出为 - 1 。
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        length = len(nums)
        for i in range(length):
            key = 0
            while nums[i]:
                key += nums[i] % 10
                nums[i] //= 10
            if key == i:
                ans = i
                break
        return ans
