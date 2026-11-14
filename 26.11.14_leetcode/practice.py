# 2026.11.14力扣网刷题
# 3364. 最小正和子数组——中级工程师、数组、前缀和、滑动窗口、第425场周赛——简单
# 给你一个整数数组 nums 和 两个 整数 l 和 r。你的任务是找到一个长度在 l 和 r 之间（包含）且和大于 0 的 子数组 的 最小 和。
# 返回满足条件的子数组的 最小 和。如果不存在这样的子数组，则返回 - 1。
# 子数组 是数组中的一个连续 非空 元素序列。
# 示例 1：
# 输入： nums = [3, -2, 1, 4], l = 2, r = 3
# 输出： 1
# 解释：
# 长度在 l = 2 和 r = 3 之间且和大于 0 的子数组有：
# [3, -2] 和为 1
# [1, 4] 和为 5
# [3, -2, 1] 和为 2
# [-2, 1, 4] 和为 3
# 其中，子数组[3, -2] 的和为 1，是所有正和中最小的。因此，答案为 1。
# 示例 2：
# 输入： nums = [-2, 2, -3, 1], l = 2, r = 3
# 输出： - 1
# 解释：
# 不存在长度在 l 和 r 之间且和大于 0 的子数组。因此，答案为 - 1。
# 示例 3：
# 输入： nums = [1, 2, 3, 4], l = 2, r = 4
# 输出： 3
# 解释：
# 子数组[1, 2] 的长度为 2，和为 3，是所有正和中最小的。因此，答案为 3。
# 提示：
# 1 <= nums.length <= 100
# 1 <= l <= r <= nums.length
# - 1000 <= nums[i] <= 1000
from typing import List
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        Silding_Window = [0] * (r - l + 1)
        Min_Prefix = [0] * (n + 1)
        for i in range(0, n + 1):
            begin, end = i - r, i - l
            if end < 0:
                continue
            # 滑动窗口
            j, z = begin, 0
            while j <= end:
                if j < 0:
                    j += 1
                    continue
                Silding_Window[z] = prefix[j]
                j += 1
                z += 1
            j = 0
            ma = Silding_Window[0]
            while j < (r - l + 1):
                if ma < Silding_Window[j] < prefix[i] or ma >= prefix[i]:
                    ma = Silding_Window[j]
                j += 1
            # 记录最小前缀和
            if ma >= prefix[i]:
                if i == 0:
                    Min_Prefix[i] = -1
                else:
                    Min_Prefix[i] = Min_Prefix[i - 1]
            else:
                Min_Prefix[i] = prefix[i] - ma
        ans = -1
        for i in range(n + 1):
            if 0 < Min_Prefix[i] and (ans <= 0 or Min_Prefix[i] < ans):
                ans = Min_Prefix[i]
        return ans