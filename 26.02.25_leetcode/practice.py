# 2026.02.25力扣网刷题
# 257. 二叉树的所有路径——树、深度优先搜索、字符串、回溯、二叉树——简单
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [1, 2, 3, null, 5]
# 输出：["1->2->5", "1->3"]
# 示例 2：
# 输入：root = [1]
# 输出：["1"]
# 提示：
# 树中节点的数目在范围[1, 100] 内
# - 100 <= Node.val <= 100

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []
        parent = []
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                if len(parent) == 0:
                    paths.append(str(node.val))
                else:
                    paths.append(parent[-1] + '->' + str(node.val))
                return
            if len(parent) == 0:
                parent.append(str(node.val))
            else:
                parent.append(parent[-1] + '->' + str(node.val))
            dfs(node.left)
            dfs(node.right)
            parent.pop(-1)
        dfs(root)
        return paths