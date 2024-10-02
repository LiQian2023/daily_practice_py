# 2024.10.02力扣网刷题
# 数组中的第K个最大元素——数组、分治、快速选择、排序、堆（优先队列）——中等
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1:
# 输入: [3, 2, 1, 5, 6, 4] , k = 2
# 输出 : 5
# 示例 2 :
# 输入 : [3, 2, 3, 1, 2, 4, 5, 5, 6] , k = 4
# 输出 : 4
# 提示：
# 1 <= k <= nums.length <= 10^5
# - 10^4 <= nums[i] <= 10^4

class Solution(object):
    def Adjust_Down(self, a, n, parent):
        child = parent * 2 + 1
        while child < n:
            if child + 1 < n and a[child] > a[child + 1]:
                child += 1
            if a[parent] > a[child]:
                a[parent], a[child] = a[child], a[parent]
            parent = child
            child = parent * 2 + 1
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 方法一：堆
        tmp = [0] * k
        # 获取前k个数
        for i in range(k):
            tmp[i] = nums[i]
        # 找最大，建小堆
        parent = (k - 1) // 2
        while parent >= 0:
            Solution().Adjust_Down(tmp, k, parent)
            parent -= 1
        # 从剩下的N-k个元素中找最大
        length = len(nums)
        for i in range(k, length):
            if nums[i] > tmp[0]:
                tmp[0] = nums[i]
                Solution().Adjust_Down(tmp, k, 0)
        return tmp[0]


nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))