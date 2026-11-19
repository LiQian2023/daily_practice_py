# 2026.11.19力扣网刷题
# 2567. 修改两个元素的最小分数——高级工程师、贪心、数组、排序、第98场双周赛——中等
# 给你一个下标从 0 开始的整数数组 nums 。
# nums 的 最小 得分是满足 0 <= i < j < nums.length 的 | nums[i] - nums[j] | 的最小值。
# nums的 最大 得分是满足 0 <= i < j < nums.length 的 | nums[i] - nums[j] | 的最大值。
# nums 的分数是 最大 得分与 最小 得分的和。
# 我们的目标是最小化 nums 的分数。你 最多 可以修改 nums 中 2 个元素的值。
# 请你返回修改 nums 中 至多两个 元素的值后，可以得到的 最小分数 。
# | x | 表示 x 的绝对值。
# 示例 1：
# 输入：nums = [1, 4, 3]
# 输出：0
# 解释：将 nums[1] 和 nums[2] 的值改为 1 ，nums 变为[1, 1, 1] 。 | nums[i] - nums[j] | 的值永远为 0 ，所以我们返回 0 + 0 = 0 。
# 示例 2：
# 输入：nums = [1, 4, 7, 8, 5]
# 输出：3
# 解释：
# 将 nums[0] 和 nums[1] 的值变为 6 ，nums 变为[6, 6, 7, 8, 5] 。
# 最小得分是 i = 0 且 j = 1 时得到的 | nums[i] - nums[j] | = | 6 - 6 | = 0 。
# 最大得分是 i = 3 且 j = 4 时得到的 | nums[i] - nums[j] | = | 8 - 5 | = 3 。
# 最大得分与最小得分之和为 3 。这是最优答案。
# 提示：
# 3 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
from typing import List
class Solution:
    def AdjustDown_MinHeap(self, nums, n, parent):
        child = parent * 2 + 1
        while child < n:
            if child + 1 < n and nums[child]>nums[child + 1]:
                child += 1
            if nums[child] >= nums[parent]:
                break
            nums[child], nums[parent] = nums[parent], nums[child]
            parent = child
            child = parent * 2 + 1
    
    def AdjustDown_MaxHeap(self, nums, n, parent):
        child = parent * 2 + 1
        while child < n:
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if nums[child] <= nums[parent]:
                break
            nums[child], nums[parent] = nums[parent], nums[child]
            parent = child
            child = parent * 2 + 1
    
    def CreateMinHeap(self, nums, n):
        for i in range((n - 1) // 2, -1, -1):
            self.AdjustDown_MinHeap(nums, n, i)
    
    def CreateMaxHeap(self, nums, n):
        for i in range((n - 1) // 2, -1, -1):
            self.AdjustDown_MaxHeap(nums, n, i)
    
    def MinHeapSort(self, nums, n):
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.AdjustDown_MinHeap(nums, i, 0)
    
    def MaxHeapSort(self, nums, n):
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.AdjustDown_MaxHeap(nums, i, 0)
            
    def minimizeSum(self, nums: List[int]) -> int:
        maxHeap, minHeap = [nums[-1], nums[-2], nums[-3]], [nums[0], nums[1], nums[2]]
        self.CreateMaxHeap(minHeap, 3)
        self.CreateMinHeap(maxHeap, 3)
        n = len(nums)
        for i in range(0, n):
            if i > 2 and nums[i] < minHeap[0]:
                minHeap[0] = nums[i]
                self.AdjustDown_MaxHeap(minHeap, 3, 0)
            if i < n - 3 and nums[i] > maxHeap[0]:
                maxHeap[0] = nums[i]
                self.AdjustDown_MinHeap(maxHeap, 3, 0)
        self.MaxHeapSort(minHeap, 3)
        self.MinHeapSort(maxHeap, 3)
        a, b, c = maxHeap[0] - minHeap[2], maxHeap[2] - minHeap[0], maxHeap[1] - minHeap[1]
        return min(a, b, c)
        