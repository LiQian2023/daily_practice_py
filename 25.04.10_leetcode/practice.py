# 2025.04.10力扣网刷题
# 唯一元素的和——数组、哈希表、计数——简单
# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
# 请你返回 nums 中唯一元素的 和 。
# 示例 1：
# 输入：nums = [1, 2, 3, 2]
# 输出：4
# 解释：唯一元素为[1, 3] ，和为 4 。
# 示例 2：
# 输入：nums = [1, 1, 1, 1, 1]
# 输出：0
# 解释：没有唯一元素，和为 0 。
# 示例 3 ：
# 输入：nums = [1, 2, 3, 4, 5]
# 输出：15
# 解释：唯一元素为[1, 2, 3, 4, 5] ，和为 15 。
# 提示：
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        max_num, min_num = nums[0], nums[0]
        for i in range(1, length):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[i])
        size = max_num - min_num + 1
        hash = [0] * size
        for num in nums:
            key = num - min_num
            hash[key] += 1
        ans = 0
        for i in range(size):
            if hash[i] == 1:
                ans += i + min_num
        return ans