# 2025.06.03力扣网刷题
# 二叉搜索树节点最小距离——树、深度优先搜索、广度优先搜索、二叉搜索树、二叉树——简单
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
# 示例 1：
# 输入：root = [4, 2, 6, 1, 3]
# 输出：1
# 示例 2：
# 输入：root = [1, 0, 48, null, null, 12, 49]
# 输出：1
# 提示：
# 树中节点的数目范围是[2, 100]
# 0 <= Node.val <= 10^5
# 注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        tmp = [1]
        def dfs(root):
            if root:
                dfs(root.left)
                tmp.append(root.val)
                tmp[0] += 1
                dfs(root.right)
        dfs(root)
        ans = abs(tmp[1] - tmp[2])
        for i in range(2, tmp[0]):
            ans = min(ans, abs(tmp[i] - tmp[i-1]))
        return ans