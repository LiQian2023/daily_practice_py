# 2026.05.05力扣网刷题
# 61. 旋转链表——链表、双指针——中等
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 示例 1：
# 输入：head = [1, 2, 3, 4, 5], k = 2
# 输出：[4, 5, 1, 2, 3]
# 示例 2：
# 输入：head = [0, 1, 2], k = 4
# 输出：[2, 0, 1]
# 提示：
# 链表中节点的数目在范围[0, 500] 内
# - 100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
from asyncio.windows_events import NULL
from contextlib import nullcontext


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def getSize(node):
            if not node:
                return 0
            return 1 + getSize(node.next)
        size = getSize(head)
        if size == 0 or k % size == 0:
            return head
        n = size - k % size
        pre, cur = head, head.next
        for i in range(1, n):
            pre = cur
            cur = cur.next
        pre.next = None
        pre = cur
        while cur and cur.next:
            cur = cur.next
        cur.next = head
        head = pre
        return head