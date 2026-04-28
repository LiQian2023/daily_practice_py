# 2026.04.28力扣网刷题
# 面试题 04.04.检查平衡性——树、深度优先搜索、二叉树——简单
# 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
# 示例 1：
# 给定二叉树[3, 9, 20, null, null, 15, 7]
# 3
# / \
# 9  20
# / \
# 15   7
# 返回 true 。
# 示例 2：
# 给定二叉树[1, 2, 2, 3, 3, null, null, 4, 4]
# 1
# / \
# 2   2
# / \
# 3   3
# / \
# 4   4
# 返回 false 。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            return max(left, right) + 1
        
        def check(root):
            if not root:
                return True
            l = dfs(root.left)
            r = dfs(root.right)
            res = abs(l - r) <= 1
            return check(root.left) and check(root.right) and res
        return check(root)