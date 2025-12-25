# 2025.12.25力扣网刷题
# 3105. 最长的严格递增或递减子数组——数组、第392场周赛——简单
# 给你一个整数数组 nums 。
# 返回数组 nums 中 严格递增 或 严格递减 的最长非空子数组的长度。
# 示例 1：
# 输入：nums = [1, 4, 3, 3, 2]
# 输出：2
# 解释：
# nums 中严格递增的子数组有[1]、[2]、[3]、[3]、[4] 以及[1, 4] 。
# nums 中严格递减的子数组有[1]、[2]、[3]、[3]、[4]、[3, 2] 以及[4, 3] 。
# 因此，返回 2 。
# 示例 2：
# 输入：nums = [3, 3, 3, 3]
# 输出：1
# 解释：
# nums 中严格递增的子数组有[3]、[3]、[3] 以及[3] 。
# nums 中严格递减的子数组有[3]、[3]、[3] 以及[3] 。
# 因此，返回 1 。
# 示例 3：
# 输入：nums = [3, 2, 1]
# 输出：3
# 解释：
# nums 中严格递增的子数组有[3]、[2] 以及[1] 。
# nums 中严格递减的子数组有[3]、[2]、[1]、[3, 2]、[2, 1] 以及[3, 2, 1] 。
# 因此，返回 3 。
# 提示：
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ret, l, r = 0, 0, 1
        flag = True # 升序
        while r <= length:
            # 升降改变标志
            change = 0
            # 升序变降序
            if r < length and flag and nums[r - 1] > nums[r]:
                flag = False
                change = 1
            # 降序变升序
            elif r < length and flag == False and nums[r - 1] < nums[r]:
                flag = True
                change = 2
            # 不升不降处理
            elif r < length and nums[r - 1] == nums[r]:
                change = 3
            if r - l > ret:
                ret = r - l
            # 状态发生变化，更新边界
            if change:
                if change == 3:
                    l = r
                else:
                    l = r - 1
            r += 1
        return ret
