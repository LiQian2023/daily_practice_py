# 2026.04.18力扣网刷题
# LCR 174. 寻找二叉搜索树中的目标节点——树、深度优先搜索、二叉搜索树、二叉树——简单
# 某公司组织架构以二叉搜索树形式记录，节点值为处于该职位的员工编号。请返回第 cnt 大的员工编号。
# 示例 1：
# 输入：root = [7, 3, 9, 1, 5], cnt = 2
# 7
# / \
# 3   9
# / \
# 1   5
# 输出：7
# 示例 2：
# 输入: root = [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8], cnt = 4
# 10
# / \
# 5   15
# / \    \
# 2   7    20
# /   / \
# 1   6   8
# 输出: 8
# 提示：
# 1 ≤ cnt ≤ 二叉搜索树元素个数

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def findTargetNode(self, root, cnt):
        """
        :type root: Optional[TreeNode]
        :type cnt: int
        :rtype: int
        """
        self.ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.ans[-cnt]