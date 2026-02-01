# 2026.02.01力扣网刷题
# 面试题 17.10.主要元素——数组、计数——简单
# 数组中占比超过一半的元素称之为主要元素。给你一个 整数 数组，找出其中的主要元素。若没有，返回 - 1 。请设计时间复杂度为 O(N) 、空间复杂度为 O(1) 的解决方案。
# 示例 1：
# 输入：[1, 2, 5, 9, 5, 9, 5, 5, 5]
# 输出：5
# 示例 2：
# 输入：[3, 2]
# 输出： - 1
# 示例 3：
# 输入：[2, 2, 1, 1, 1, 2, 2]
# 输出：2

class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
        ans, length = -1, len(nums) // 2
        for key, val in hash.items():
            if val > length:
                ans = key
                break
        return ans

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elem, count = 0, 0
        for num in nums:
            if count == 0:
                elem = num
            if num == elem:
                count += 1
            else:
                count -= 1
        count = nums.count(elem)
        return elem if count > len(nums) // 2 else -1