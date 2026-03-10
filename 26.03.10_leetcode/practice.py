# 2026.03.10力扣网刷题
# 938. 二叉搜索树的范围和——高级工程师、树、深度优先搜索、二叉搜索树、二叉树、第110场周赛——简单
# 给定二叉搜索树的根结点 root，返回值位于范围[low, high] 之间的所有结点的值的和。
# 示例 1：
# 输入：root = [10, 5, 15, 3, 7, null, 18], low = 7, high = 15
# 输出：32
# 示例 2：
# 输入：root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], low = 6, high = 10
# 输出：23
# 提示：
# 树中节点数目在范围[1, 2 * 10^4] 内
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# 所有 Node.val 互不相同

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        self.sum = 0
        def dfs(node, low, high):
            if not node:
                return
            if low <= node.val <= high:
                self.sum += node.val
            if low <= node.val:
                dfs(node.left, low, high)
            if node.val <= high:
                dfs(node.right, low, high)
        dfs(root, low, high)
        return self.sum