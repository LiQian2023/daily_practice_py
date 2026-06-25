# 2026.06.25力扣网刷题
# LCR 193. 二叉搜索树的最近公共祖先——树、深度优先搜索、二叉搜索树、二叉树——简单
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉搜索树 : root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
# 示例 1：
# 输入：root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# 输出：6
# 解释：节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2：
# 输入：root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
# 输出：2
# 解释：节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 说明：
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
# 注意：本题与主站 235 题相同：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, stack, key):
        if root is None:
            return
        stack.append(root)
        if root.val == key:
            return
        if root.val < key:
            self.dfs(root.right, stack, key)
        else:
            self.dfs(root.left, stack, key)
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack1, stack2 = [], []
        self.dfs(root, stack1, p.val)
        self.dfs(root, stack2, q.val)
        ans = None
        i, j = 0, 0
        len1, len2 = len(stack1), len(stack2)
        while i < len1 and j < len2:
            if stack1[i] == stack2[j]:
                ans = stack1[i]
            i += 1
            j += 1
        return ans