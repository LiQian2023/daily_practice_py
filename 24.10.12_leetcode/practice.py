# 2024.10.12力扣网刷题
# 求出出现两次数字的 XOR 值——位运算、数组、哈希表——简单
# 给你一个数组 nums ，数组中的数字 要么 出现一次，要么 出现两次。
# 请你返回数组中所有出现两次数字的按位 XOR 值，如果没有数字出现过两次，返回 0 。
# 示例 1：
# 输入：nums = [1, 2, 1, 3]
# 输出：1
# 解释：
# nums 中唯一出现过两次的数字是 1 。
# 示例 2：
# 输入：nums = [1, 2, 3]
# 输出：0
# 解释：
# nums 中没有数字出现两次。
# 示例 3：
# 输入：nums = [1, 2, 2, 1]
# 输出：3
# 解释：
# 数字 1 和 2 出现过两次。1 XOR 2 == 3 。
# 提示：
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# nums 中每个数字要么出现过一次，要么出现过两次。


class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法一：哈希表
        my_list = list(set(nums))
        length = len(my_list)
        i = 0
        while i < length:
            if nums.count(my_list[i]) == 1:
                my_list.remove(my_list[i])
                length -= 1
                continue
            i += 1
        ans = 0
        for num in my_list:
            ans ^= num
        return ans


nums = [1,2,3,1]
print(Solution().duplicateNumbersXOR(nums))