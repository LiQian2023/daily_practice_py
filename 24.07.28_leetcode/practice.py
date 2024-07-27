# 2024.07.28力扣网刷题
# 存在重复元素 II——数组、哈希表、滑动窗口——简单
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，
# 满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：nums = [1, 2, 3, 1], k = 3
# 输出：true
# 示例 2：
# 输入：nums = [1, 0, 1, 1], k = 1
# 输出：true
# 示例 3：
# 输入：nums = [1, 2, 3, 1, 2, 3], k = 2
# 输出：false
# 提示：
# 1 <= nums.length <= 10^5
# - 10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 哈希表
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                if i - my_dict[nums[i]] <= k:
                    return True
                elif i - my_dict[nums[i]] > k:
                    my_dict[nums[i]] = i
            else:
                my_dict[nums[i]] = i
        return False