# 2024.11.15力扣网刷题
# 判断对称二叉树——树、深度优先搜索、广度优先搜索、二叉树——简单
# 请设计一个函数判断一棵二叉树是否 轴对称 。
# 示例 1：
# 输入：root = [6, 7, 7, 8, 9, 9, 8]
# 输出：true
# 解释：从图中可看出树是轴对称的。
# 示例 2：
# 输入：root = [1, 2, 2, null, 3, null, 3]
# 输出：false
# 解释：从图中可看出最后一层的节点不对称。
# 提示：
# 0 <= 节点个数 <= 1000
# 注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def checkSymmetricTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            if left and not right or not left and right:
                return False
            if left.val != right.val:
                return False
            ret1 = dfs(left.left, right.right)
            ret2 = dfs(left.right, right.left)
            return ret1 and ret2
        return dfs(root.left, root.right)

