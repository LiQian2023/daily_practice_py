# 2025.02.02力扣网刷题
# 区间加法 II——数组、数学——简单
# 给你一个 m x n 的矩阵 M 和一个操作数组 op 。矩阵初始化时所有的单元格都为 0 。ops[i] = [ai, bi] 意味着当所有的 0 <= x < ai 和 0 <= y < bi 时， M[x][y] 应该加 1。
# 在 执行完所有操作后 ，计算并返回 矩阵中最大整数的个数 。
# 示例 1:
# 输入: m = 3, n = 3，ops = [[2, 2], [3, 3]]
# 输出 : 4
# 解释 : M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。
# 示例 2 :
# 输入 : m = 3, n = 3, ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
# 输出 : 4
# 示例 3 :
# 输入 : m = 3, n = 3, ops = []
# 输出 : 9
# 提示 :
# 1 <= m, n <= 4 * 10^4
# 0 <= ops.length <= 10^4
# ops[i].length == 2
# 1 <= ai <= m
# 1 <= bi <= n

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        length = len(ops)
        min_x = m
        min_y = n
        for i in range(length):
            min_x = min(min_x, ops[i][0])
            min_y = min(min_y, ops[i][1])
        return min_x * min_y