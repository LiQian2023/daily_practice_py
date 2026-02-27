# 2026.02.27力扣网刷题
# 501. 二叉搜索树中的众数——树、深度优先搜索、二叉搜索树、二叉树——简单
# 给你一个含重复值的二叉搜索树（BST）的根节点 root ，找出并返回 BST 中的所有 众数（即，出现频率最高的元素）。
# 如果树中有不止一个众数，可以按 任意顺序 返回。
# 假定 BST 满足如下定义：
# 结点左子树中所含节点的值 小于等于 当前节点的值
# 结点右子树中所含节点的值 大于等于 当前节点的值
# 左子树和右子树都是二叉搜索树
# 示例 1：
# 输入：root = [1, null, 2, 2]
# 输出：[2]
# 示例 2：
# 输入：root = [0]
# 输出：[0]
# 提示：
# 树中节点的数目在范围[1, 10^4] 内
# - 10^5 <= Node.val <= 10^5
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)

        if self.parent == None or self.parent != root.val:
            self.count = 1
        else:
            self.count += 1
        if self.count > self.mode:
            self.ans = [root.val]
            self.mode = self.count
        elif self.count == self.mode:
            self.ans.append(root.val)

        self.parent = root.val

        self.dfs(root.right)
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 思路：
        # 1. 判断左子树是否与根节点相等
        # 2. 判断右子树是否与根节点相等
        # 3. 返回根节点的数量
        self.mode = 0
        self.parent = None
        self.count = 0
        self.ans = []
        self.dfs(root)
        return self.ans