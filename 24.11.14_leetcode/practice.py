# 2024.11.14力扣网刷题
# 翻转二叉树——树、深度优先搜索、广度优先搜索、二叉树——简单
# 给定一棵二叉树的根节点 root，请左右翻转这棵二叉树，并返回其根节点。
# 示例 1：
# 输入：root = [5, 7, 9, 8, 3, 2, 4]
# 输出：[5, 9, 7, 4, 2, 3, 8]
# 提示：
# 树中节点数目范围在[0, 100] 内
# - 100 <= Node.val <= 100
# 注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flipTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def flip(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            flip(root.left)
            flip(root.right)

        flip(root)
        return root
