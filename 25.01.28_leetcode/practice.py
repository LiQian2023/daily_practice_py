# 2025.01.28力扣网刷题
# 杨辉三角 II——数组、动态规划——简单
# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
# 示例 1:
# 输入: rowIndex = 3
# 输出 : [1, 3, 3, 1]
# 示例 2 :
# 输入 : rowIndex = 0
# 输出 : [1]
# 示例 3 :
# 输入 : rowIndex = 1
# 输出 : [1, 1]
# 提示 :
# 0 <= rowIndex <= 33
# 进阶：
# 你可以优化你的算法到 O(rowIndex) 空间复杂度吗？

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1] * (rowIndex + 1)
        for level in range(2, rowIndex + 1):
            tmp = ans[:level]
            for i in range(1, level):
                ans[i] = tmp[i - 1] + tmp[i]
        return ans