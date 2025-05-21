# 2025.05.21力扣网刷题
# 两数之和 IV - 输入二叉搜索树——树、深度优先搜索、广度优先搜索、二叉搜索树、哈希表、双指针、二叉树——简单
# 给定一个二叉搜索树 root 和一个目标结果 k，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 示例 1：
# 输入 : root = [5, 3, 6, 2, 4, null, 7], k = 9
# 输出 : true
# 示例 2：
# 输入 : root = [5, 3, 6, 2, 4, null, 7], k = 28
# 输出 : false
# 提示 :
# 二叉树的节点个数的范围是[1, 10^4].
# - 10^4 <= Node.val <= 10^4
# 题目数据保证，输入的 root 是一棵 有效 的二叉搜索树
# - 10^5 <= k <= 10^5

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        hash = {}
        def dfs(root):
            if root:
                if root.val in hash:
                    hash[root.val] += 1
                else:
                    hash[root.val] = 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        for key in hash:
            key2 = k - key
            if key2 in hash:
                if key != key2 or hash[key] > 1:
                    return True
        return False