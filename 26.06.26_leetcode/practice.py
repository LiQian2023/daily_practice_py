# 2026.06.26力扣网刷题
# LCR 194. 二叉树的最近公共祖先——树、深度优先搜索、二叉树——简单
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树 : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
# 示例 1：
# 输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2：
# 输入：root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 说明：
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
# 注意：本题与主站 236 题相同：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        stack1, stack2 = [], []
        flag1, flag2 = False, False
        stack1, flag1 = self.dfs(root, stack1, p, flag1)
        self.Print(stack1)
        stack2, flag2 = self.dfs(root, stack2, q, flag2)
        self.Print(stack2)
        i, j = 0, 0
        len1, len2 = len(stack1), len(stack2)
        ans = None
        while i < len1 and j < len2:
            if stack1[i] == stack2[j]:
                ans = stack1[i]
            i += 1
            j += 1
        return ans

    def dfs(self, root, stack, target, flag):
        if not root:
            return stack, flag
        stack.append(root)
        if root.val == target.val:
            flag = True
            return stack, flag
        if not flag:
            stack, flag = self.dfs(root.left, stack, target, flag)
        if not flag:
            stack, flag = self.dfs(root.right, stack, target, flag)
        if not flag:
            stack.pop()
        return stack, flag

    def Print(self, stack):
        for node in stack:
            print(node.val, end=" ")
        print('')