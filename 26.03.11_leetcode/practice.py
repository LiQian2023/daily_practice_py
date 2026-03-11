# 2026.03.11力扣网刷题
# 703. 数据流中的第 K 大元素——树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）——简单
# 设计一个找到数据流中第 k 大元素的类（class）。
# 注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
# 示例 1：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：[null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3); // 返回 4
# kthLargest.add(5); // 返回 5
# kthLargest.add(10); // 返回 5
# kthLargest.add(9); // 返回 8
# kthLargest.add(4); // 返回 8
# 示例 2：
# 输入：
# ["KthLargest", "add", "add", "add", "add"]
# [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
# 输出：[null, 7, 7, 7, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
# kthLargest.add(2); // 返回 7
# kthLargest.add(10); // 返回 7
# kthLargest.add(9); // 返回 7
# kthLargest.add(9); // 返回 8
# 提示：
# 0 <= nums.length <= 10^4
# 1 <= k <= nums.length + 1
# - 10^4 <= nums[i] <= 10^4
# - 10^4 <= val <= 10^4
# 最多调用 add 方法 10^4 次


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        self.len = 0
        for num in nums:
            if self.len < self.k:
                self.heap.append(num)
                self.len += 1
                if self.len == self.k:
                    self.CreateHeap()
            else:
                if num > self.heap[0]:
                    self.heap[0] = num
                    self.AdjustDown(0)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.len < self.k:
            self.heap.append(val)
            self.len += 1
            if self.len == self.k:
                self.CreateHeap()
            else:
                return min(self.heap)
        else:
            if val > self.heap[0]:
                self.heap[0] = val
                self.AdjustDown(0)
        return self.heap[0]

    def AdjustDown(self, parent):
        child = parent * 2 + 1
        while child < self.len:
            if child + 1 < self.len and self.heap[child] > self.heap[child + 1]:
                child += 1
            if self.heap[child] < self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                parent = child
                child = parent * 2 + 1
            else:
                break

    def CreateHeap(self):
        for i in range((self.len - 1) // 2, -1, -1):
            self.AdjustDown(i)