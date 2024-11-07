# 2024.11.07力扣网刷题
# 长度为 K 的子数组的能量值 II——数组、滑动窗口——中等
# 给你一个长度为 n 的整数数组 nums 和一个正整数 k 。
# 一个数组的 能量值 定义为：
# 如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
# 否则为 - 1 。
# 你需要求出 nums 中所有长度为 k 的子数组的能量值。
# 请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。
# 示例 1：
# 输入：nums = [1, 2, 3, 4, 3, 2, 5], k = 3
# 输出：[3, 4, -1, -1, -1]
# 解释：
# nums 中总共有 5 个长度为 3 的子数组：
# [1, 2, 3] 中最大元素为 3 。
# [2, 3, 4] 中最大元素为 4 。
# [3, 4, 3] 中元素 不是 连续的。
# [4, 3, 2] 中元素 不是 上升的。
# [3, 2, 5] 中元素 不是 连续的。
# 示例 2：
# 输入：nums = [2, 2, 2, 2, 2], k = 4
# 输出：[-1, -1]
# 示例 3：
# 输入：nums = [3, 2, 3, 2, 3, 2], k = 2
# 输出：[-1, 3, -1, 3, -1]
# 提示：
# 1 <= n == nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= n


class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        i, n = 0, 1
        ans = []
        size, base = 0, length - k + 1
        while i < length and size < base:
            if n == k:
                ans.append(nums[i])
                size += 1
                n -= 1
            else:
                if i and nums[i] != nums[i-1] + 1:
                    while n and size < base:
                        ans.append(-1)
                        size += 1
                        n -= 1
                elif i and nums[i] == nums[i-1] + 1:
                    n += 1
                    if n == k:
                        ans.append(nums[i])
                        size += 1
                        n -= 1
            if n == 0:
                n += 1
            i += 1
        return ans


nums = [4,4,5,1,4,1,4,5,6,1]
k = 3
print(Solution().resultsArray(nums, k))
