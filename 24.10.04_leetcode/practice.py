# 2024.10.04力扣网刷题
# 摆动排序 II——贪心、数组、分治、快速选择、排序——中等
# 给你一个整数数组nums，将它重新排列成
# nums[0] < nums[1] > nums[2] < nums[3]...的顺序。
# 你可以假设所有输入数组都可以得到满足题目要求的结果。
# 示例1：
# 输入：nums = [1, 5, 1, 1, 6, 4]
# 输出：[1, 6, 1, 5, 1, 4]
# 解释：[1, 4, 1, 5, 1, 6]
# 同样是符合题目要求的结果，可以被判题程序接受。
# 示例2：
# 输入：nums = [1, 3, 2, 2, 3, 1]
# 输出：[2, 3, 1, 3, 1, 2]
# 提示：
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5000
# 题目数据保证，对于给定的输入nums ，总能产生满足题目要求的结果
# 进阶：你能用O(n)时间复杂度和 / 或原地O(1)额外空间来实现吗？


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_list = sorted(set(nums))
        my_dict = dict(zip(nums_list, [nums.count(i) for i in nums_list]))
        length1 = len(nums)
        length2 = len(nums_list)
        n = 1
        for i in range(length2 - 1, -1, -1):
            while my_dict[nums_list[i]] and n < length1:
                nums[n] = nums_list[i]
                n += 2
                my_dict[nums_list[i]] -= 1
            if n >= length1:
                break
        n -= 1
        if n >= length1:
            n -= 2
        for i in range(length2):
            while my_dict[nums_list[i]] and n < length1:
                nums[n] = nums_list[i]
                n -= 2
                my_dict[nums_list[i]] -= 1
            if n >= length1:
                break


nums = [7,9,0,6,0]
print(Solution().wiggleSort(nums))
