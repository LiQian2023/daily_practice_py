# 2026.10.22力扣网刷题
# 3942. 排序排列的最少操作数——资深工程师、数组、第503场周赛——中等
# 给你一个长度为 n 的整数数组 nums，其中 nums 是区间[0..n - 1] 中所有数字的一个排列。
# 你 只能 执行以下操作：
# 反转 整个数组。
# 左旋一位：将第一个元素移动到数组末尾，其余元素整体向左移动一位。
# 返回将数组按 递增 顺序排序所需的 最少 操作次数。如果仅使用给定操作无法将数组排序，则返回 - 1。
# 排列 是数组中所有元素的一种重新排列。
# 示例 1：
# 输入： nums = [0, 2, 1]
# 输出： 2
# 解释：
# 左旋一位：[2, 1, 0]
# 反转数组：[0, 1, 2]
# 数组在 2 次操作后变为有序，这是最少操作次数。
# 示例 2：
# 输入： nums = [1, 0, 2]
# 输出： 2
# 解释：
# 反转数组：[2, 0, 1]
# 左旋一位：[0, 1, 2]
# 数组在 2 次操作后变为有序，这是最少操作次数。
# 示例 3：
# 输入： nums = [2, 0, 1, 3]
# 输出： - 1
# 解释：
# 无法将该数组变为[0, 1, 2, 3]。因此答案为 - 1。
# 提示：
# 1 <= n == nums.length <= 10^5
# 0 <= nums[i] <= n - 1
# nums 是从 0 到 n - 1 的整数排列。
from typing import List
class Solution:
    def check(self, nums, size, flag, begin):
        i = begin
        while 1:
            if (i + 1) % size == begin:
                break
            if (nums[i] - nums[(i + 1) % size]) * flag > 0:
                return 0
            i = (i + 1) % size
        return 1
    
    def minOperations(self, nums: List[int]) -> int:
        ma, mi, n = 0, 0, len(nums)
        for i in range(n):
            if nums[i] > nums[ma]:
                ma = i
            elif nums[i] < nums[mi]:
                mi = i
        increase, decrease = self.check(nums, n, 1, mi), self.check(nums, n, -1, ma)
        ans = -1
        if increase:
            op1, op2 = mi, n - mi + 2
            ans = op1 if op1 < op2 else op2
        if decrease:
            op1, op2 = ma + 1, n - ma + 1
            if ans != -1:
                ans = ans if ans < op1 else op1
                ans = ans if ans < op2 else op2
            else:
                ans = op1 if op1 < op2 else op2
        return ans