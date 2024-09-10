# 2024.09.10力扣网刷题——2024.01.10C语言完成解题
# 多数元素——数组、哈希表、计数、排序、分治——简单
# 给定一个大小为n的数组nums ，返回其中的多数元素。
# 多数元素是指在数组中出现次数大于 ⌊ n / 2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例
# 1：
# 输入：nums = [3, 2, 3]
# 输出：3
# 示例
# 2：
# 输入：nums = [2, 2, 1, 1, 1, 2, 2]
# 输出：2
# 提示：
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# 进阶：尝试设计时间复杂度为O(n)、空间复杂度为O(1)的算法解决此问题。

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：哈希表
        length = len(nums)
        key = length // 2
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
            if nums_dict[num] > key:
                key = num
                break
        return key