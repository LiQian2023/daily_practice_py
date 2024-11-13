# 2024.11.13力扣网刷题
# 平衡二叉树——树、深度优先搜索、二叉树——简单
# 给定一个二叉树，判断它是否是平衡二叉树
# 示例 1：
# 输入：root = [3, 9, 20, null, null, 15, 7]
# 输出：true
# 示例 2：
# 输入：root = [1, 2, 2, 3, 3, null, null, 4, 4]
# 输出：false
# 示例 3：
# 输入：root = []
# 输出：true
# 提示：
# 树中的节点数在范围[0, 5000] 内
# - 10^4 <= Node.val <= 10^4

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
            if not root.left and not root.right:
                root.val = 0
                return 1
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            root.val = left - right
            return max(left, right)
        def dfs2(root):
            if not root:
                return True
            if root.val > 1 or root.val < -1:
                return False
            left = dfs2(root.left)
            right = dfs2(root.right)
            return left & right
        ret = dfs(root)
        return dfs2(root)