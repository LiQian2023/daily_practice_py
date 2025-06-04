# 2025.06.04力扣网刷题
# 二叉树的堂兄弟节点——树、深度优先搜索、广度优先搜索、二叉树——简单
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k + 1 处。
# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。
# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。
# 示例 1：
# 输入：root = [1, 2, 3, 4], x = 4, y = 3
# 输出：false
# 示例 2：
# 输入：root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4
# 输出：true
# 示例 3：
# 输入：root = [1, 2, 3, null, 4], x = 2, y = 3
# 输出：false
# 提示：
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        size = 100
        queue = [root] * size
        front, rear = 0, 1
        level_x, level_y = 0, 0
        parent_x, parent_y = 0, 0
        level = 1
        num, next_num = 1, 0
        while not level_x or not level_y:
            while num:
                node = queue[front]
                front = (front + 1) % size
                num -= 1
                if node.val == x:
                    level_x = level
                elif node.val == y:
                    level_y = level
                if node.left:
                    queue[rear] = node.left
                    rear = (rear + 1) % size
                    next_num += 1
                    if node.left.val == x:
                        parent_x = node.val
                    elif node.left.val == y:
                        parent_y = node.val
                if node.right:
                    queue[rear] = node.right
                    rear = (rear + 1) % size
                    next_num += 1
                    if node.right.val == x:
                        parent_x = node.val
                    elif node.right.val == y:
                        parent_y = node.val
            num = next_num
            next_num = 0
            level += 1
        return level_x == level_y and parent_x != parent_y

