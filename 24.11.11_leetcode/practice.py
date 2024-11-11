# 2024.11.11力扣网刷题
# 将有序数组转换为二叉搜索树——树、二叉搜索树、数组、分治、二叉树——简单
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵平衡二叉搜索树。
# 示例 1：
# 输入：nums = [-10, -3, 0, 5, 9]
# 输出：[0, -3, 9, -10, null, 5]
# 解释：[0, -10, 5, null, -3, null, 9] 也将被视为正确答案：
# 示例 2：
# 输入：nums = [1, 3]
# 输出：[3, 1]
# 解释：[1, null, 3] 和[3, 1] 都是高度平衡二叉搜索树。
# 提示：
# 1 <= nums.length <= 10^4
# - 10^4 <= nums[i] <= 10^4
# nums 按 严格递增 顺序排列


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def helper(nums, start, end):
            if start > end:
                return None
            mid = (end - start) // 2 + start
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

        return helper(nums, 0, len(nums)-1)

