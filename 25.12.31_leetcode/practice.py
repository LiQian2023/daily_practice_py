# 2025.12.31力扣网刷题
# 3427. 变长子数组求和——数组、前缀和、第433场周赛——简单
# 给你一个长度为 n 的整数数组 nums 。对于 每个 下标 i（0 <= i < n），
# 定义对应的子数组 nums[start ... i]（start = max(0, i - nums[i])）。
# 返回为数组中每个下标定义的子数组中所有元素的总和。
# 子数组 是数组中的一个连续、非空 的元素序列。
# 示例 1：
# 输入：nums = [2, 3, 1]
# prefix = [2, 5, 6]
# start = [max(0 - 2, 0), max(1 - 3, 0), max(2 - 1, 0)
# 输出：11
# 解释：
# 下标 i	子数组	和
# 0	nums[0] = [2]	2
# 1	nums[0 ... 1] = [2, 3]	5
# 2	nums[1 ... 2] = [3, 1]	4
# 总和	 	11
# 总和为 11 。因此，输出 11 。
# 示例 2：
# 输入：nums = [3, 1, 1, 2]
# 输出：13
# 解释：
# 下标 i	子数组	和
# 0	nums[0] = [3]	3
# 1	nums[0 ... 1] = [3, 1]	4
# 2	nums[1 ... 2] = [1, 1]	2
# 3	nums[1 ... 3] = [1, 1, 2]	4
# 总和	 	13
# 总和为 13 。因此，输出为 13 。
# 提示：
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= 1000

class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def Get_Sum_Subset(arr, start, end):
            ret = 0
            for i in range(start, end + 1):
                ret += arr[i]
            return ret
        length = len(nums)
        ans = 0
        for i in range(length):
            start = max(i - nums[i], 0)
            ans += Get_Sum_Subset(nums, start, i)
        return ans

    def subarraySum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            start = max(i - nums[i], 0)
            if i - 1 >= 0:
                prefix[i] += nums[i] + prefix[i - 1]
            else:
                prefix[i] += nums[i]
            if start - 1 >= 0:
                ans += prefix[i] - prefix[start - 1]
            else:
                ans += prefix[i]
        return ans