# 2025.11.30力扣网刷题
# 2855. 使数组成为递增数组的最少右移次数——数组、第113场双周赛——简单
# 给你一个长度为 n 下标从 0 开始的数组 nums ，数组中的元素为 互不相同 的正整数。请你返回让 nums 成为递增数组的 最少右移 次数，如果无法得到递增数组，返回 - 1 。
# 一次 右移 指的是同时对所有下标进行操作，将下标为 i 的元素移动到下标(i + 1) % n 处。
# 示例 1：
# 输入：nums = [3, 4, 5, 1, 2]
# 输出：2
# 解释：
# 第一次右移后，nums = [2, 3, 4, 5, 1] 。
# 第二次右移后，nums = [1, 2, 3, 4, 5] 。
# 现在 nums 是递增数组了，所以答案为 2 。
# 示例 2：
# 输入：nums = [1, 3, 5]
# 输出：0
# 解释：nums 已经是递增数组了，所以答案为 0 。
# 示例 3：
# 输入：nums = [2, 1, 4]
# 输出： - 1
# 解释：无法将数组变为递增数组。
# 提示：
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# nums 中的整数互不相同。

class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, n = -1, len(nums)
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if ans != -1:
                    return -1
                ans = i
        if ans == -1:
            return 0
        if nums[-1] > nums[0]:
            return -1
        return n - ans