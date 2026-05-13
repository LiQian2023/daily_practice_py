# 2026.05.13力扣网刷题
# LCR 150. 彩灯装饰记录 II——树、广度优先搜索、二叉树——简单
# 一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从左到右的顺序返回每一层彩灯编号，每一层的结果记录于一行。
# 示例 1：
# 输入：root = [8, 17, 21, 18, null, null, 6]
# 输出： [[8], [17, 21], [18, 6]]
# 提示：
# 节点总数 <= 1000
# 注意：本题与主站 102 题相同：https://leetcode.cn/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def decorateRecord(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = []
        ans = []
        if root:
            queue.append(root)
        curLevel, nextLevel = len(queue), 0
        while curLevel:
            tmp = []
            while curLevel:
                node = queue.pop(0)
                curLevel -= 1
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                    nextLevel += 1
                if node.right:
                    queue.append(node.right)
                    nextLevel += 1
            ans.append(tmp)
            curLevel = nextLevel
            nextLevel = 0
        return ans