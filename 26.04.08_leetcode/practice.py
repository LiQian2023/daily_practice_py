# 2026.04.08力扣网刷题
# LCR 059. 数据流中的第 K 大元素——树、设计、二叉搜索树、二叉树、数据流、堆（优先队列）——简单
# 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。
# 请实现 KthLargest 类：
# KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
# int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
# 示例：
# 输入：
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# 输出：
# [null, 4, 5, 5, 8, 8]
# 解释：
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
# 提示：
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# - 10^4 <= nums[i] <= 10^4
# - 10^4 <= val <= 10^4
# 最多调用 add 方法 10^4 次
# 题目数据保证，在查找第 k 大元素时，数组中至少有 k 个元素
# 注意：本题与主站 703 题相同： https ://leetcode.cn/problems/kth-largest-element-in-a-stream/

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.maxLength = k
        self.length = 0
        self.heap = []

        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.length == self.maxLength:
            if self.heap[0] < val:
                self.heap[0] = val
                self.adjustDown(
                    self.length)
        else:
            self.push(val)
        return self.heap[0]

    def push(self, val):
        self.heap.append(val)
        self.length += 1
        if self.length == self.maxLength:
            self.createHeap()

    def createHeap(self):
        for i in range((self.length - 2)//2, -1, -1):
            self.adjustDown(self.length, i)

    def adjustDown(self, length, parent=0):
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and self.heap[child] > self.heap[child+1]:
                child += 1
            if self.heap[child] < self.heap[parent]:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                parent = child
                child = 2 * parent + 1
            else:
                break



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)