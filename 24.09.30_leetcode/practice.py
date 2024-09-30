# 2024.09.30力扣网刷题
# 最大间距——数组、桶排序、基数排序、排序——中等
# 给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。如果数组元素个数小于 2，则返回 0 。
# 您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。
# 示例 1:
# 输入: nums = [3, 6, 9, 1]
# 输出 : 3
# 解释 : 排序后的数组是[1, 3, 6, 9], 其中相邻元素(3, 6) 和(6, 9) 之间都存在最大差值 3。
# 示例 2 :
# 输入 : nums = [10]
# 输出 : 0
# 解释 : 数组元素个数小于 2，因此返回 0。
# 提示 :
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        length = len(nums)
        for i in range(1, length):
            if nums[i] - nums[i-1] > ans:
                ans = nums[i] - nums[i-1]
        return ans