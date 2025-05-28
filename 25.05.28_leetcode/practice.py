# 2025.05.28力扣网刷题
# 二叉搜索树的最小绝对差——树、二叉搜索树、广度优先搜索、深度优先搜索、二叉树——简单
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
# 差值是一个正数，其数值等于两值之差的绝对值。
# 示例 1：
# 输入：root = [4, 2, 6, 1, 3]
# 输出：1
# 示例 2：
# 输入：root = [1, 0, 48, null, null, 12, 49]
# 输出：1
# 提示：
# 树中节点的数目范围是[2, 10^4]
# 0 <= Node.val <= 10^5
# 注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference1(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        tmp = []
        begin, end = root.val, root.val
        tmp_size = 0

        def dfs(root, tmp, begin, end, tmp_size):
            if root:
                tmp.append(root.val)
                tmp_size += 1
                begin = min(begin, root.val)
                end = max(end, root.val)
                tmp, begin, end, tmp_size = dfs(root.left, tmp, begin, end, tmp_size)
                tmp, begin, end, tmp_size = dfs(root.right, tmp, begin, end, tmp_size)
            return tmp, begin, end, tmp_size

        tmp, begin, end, tmp_size = dfs(root, tmp, begin, end, tmp_size)

        def count_sort(tmp, begin, end):
            Size = end - begin + 1
            hash = [0] * Size
            for num in tmp:
                key = num - begin
                hash[key] += 1
            i, j = begin, 0
            while i <= end:
                key = i - begin
                while hash[key]:
                    tmp[j] = i
                    j += 1
                    hash[key] -= 1
                i += 1
            return tmp

        tmp = count_sort(tmp, begin, end)
        ans = tmp[1] - tmp[0]
        for i in range(1, tmp_size):
            ans = min(ans, tmp[i] - tmp[i - 1])
        return ans


    def getMinimumDifference2(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        tmp = []
        tmp_size = 0
        def dfs(root, tmp, tmp_size):
            if root:
                tmp.append(root.val)
                tmp_size += 1
                tmp, tmp_size = dfs(root.left, tmp, tmp_size)
                tmp, tmp_size = dfs(root.right, tmp, tmp_size)
            return tmp, tmp_size

        tmp, tmp_size = dfs(root, tmp, tmp_size)
        tmp.sort()
        ans = tmp[1] - tmp[0]
        for i in range(1, tmp_size):
            ans = min(ans, tmp[i] - tmp[i - 1])
        return ans

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        tmp = []
        n = 0
        def in_order(root, tmp, n):
            if root.left:
                n = in_order(root.left, tmp, n)
            tmp.append(root.val)
            n += 1
            if root.right:
                n = in_order(root.right, tmp, n)
            return n
        n = in_order(root, tmp, n)
        ans = tmp[1] - tmp[0]
        for i in range(2, n):
            ans = min(ans, tmp[i] - tmp[i - 1])
        return ans