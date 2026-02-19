# 2026.02.19力扣网刷题
# LCR 056. 两数之和 IV - 输入二叉搜索树——数组、滑动窗口——简单
# 给定一个二叉搜索树的 根节点 root 和一个整数 k, 请判断该二叉搜索树中是否存在两个节点它们的值之和等于 k 。假设二叉搜索树中节点的值均唯一。
# 示例 1：
# 输入 : root = [8, 6, 10, 5, 7, 9, 11], k = 12
# 输出 : true
# 解释 : 节点 5 和节点 7 之和等于 12
# 示例 2：
# 输入 : root = [8, 6, 10, 5, 7, 9, 11], k = 22
# 输出 : false
# 解释 : 不存在两个节点值之和为 22 的节点
# 提示：
# 二叉树的节点个数的范围是[1, 10^4].
# - 10^4 <= Node.val <= 10^4
# root 为二叉搜索树
# - 10^5 <= k <= 10^5
# 注意：本题与主站 653 题相同： https ://leetcode.cn/problems/two-sum-iv-input-is-a-bst/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        tmp = []
        def dfs(root, tmp):
            if not root:
                return
            dfs(root.left, tmp)
            tmp.append(root.val)
            dfs(root.right, tmp)
        dfs(root, tmp)
        def dfs2(root, target, k):
            if not root:
                return False
            if target == root.val:
                return True
            if target < root.val:
                return dfs2(root.left, target, k)
            else:
                return dfs2(root.right, target, k)
        ans = False
        for num in tmp:
            target = k - num
            if target == num:
                continue
            ans = dfs2(root, target, k)
            if ans:
                break
        return ans