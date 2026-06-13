# 2026.06.13力扣网刷题
# LCR 052. 递增顺序搜索树——栈、树、深度优先搜索——二叉搜索树、二叉树——简单
# 给你一棵二叉搜索树，请 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
# 示例 1：
# 输入：root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
# 输出：[1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7, null, 8, null, 9]
# 示例 2：
# 输入：root = [5, 1, 7]
# 输出：[1, null, 5, null, 7]
# 提示：
# 树中节点数的取值范围是[1, 100]
# 0 <= Node.val <= 1000
# 注意：本题与主站 897 题相同： https ://leetcode.cn/problems/increasing-order-search-tree/

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def increasingBST(self, root: TreeNode) -> Optional[TreeNode]:
        def visited(node):
            if not self.newRoot:
                self.newRoot = node
            if self.pre:
                self.pre.right = node
            self.pre = node
            node.left = None
            
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            visited(node)
            dfs(node.right)
        
        self.pre = None
        self.newRoot = None
        dfs(root)
        return self.newRoot
        