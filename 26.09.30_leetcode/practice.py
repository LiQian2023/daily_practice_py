# 2026.09.30力扣网刷题
# 113. 路径总和 II——树、深度优先搜索、回溯、二叉树——中等
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
# 示例 1：
# 输入：root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1], targetSum = 22
# 输出： [[5, 4, 11, 2], [5, 8, 4, 5]]
# 示例 2：
# 输入：root = [1, 2, 3], targetSum = 5
# 输出：[]
# 示例 3：
# 输入：root = [1, 2], targetSum = 0
# 输出：[]
# 提示：
# 树中节点总数在范围[0, 5000] 内
# - 1000 <= Node.val <= 1000
# - 1000 <= targetSum <= 1000
from ast import List


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def getLevle(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.getLevle(root.left)
        r = self.getLevle(root.right)
        return l + 1 if l > r else r + 1
    def getLeave(self, root):
        if root and not root.left and not root.right:
            return 1
        if not root:
            return 0
        l = self.getLeave(root.left)
        r = self.getLeave(root.right)
        return l + r
    
class Solution:
    def dfs(self, root, path, ans, target, cur) -> None:
        if not root:
            return
        path.append(root.val)
        cur += root.val
        if not root.left and not root.right:
            if cur == target:
                ans.append(path[::])
        else:
            self.dfs(root.left, path, ans, target, cur)
            self.dfs(root.right, path, ans, target, cur)
        path.pop()
        
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        path, ans = [], []
        self.dfs(root, path, ans, targetSum, 0)
        return ans
        
        