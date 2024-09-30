# 2024.03.14力扣网刷题——2024.09.30完成解答
# 丑数 II——哈希表、数字、动态规划、堆（优先队列）——中等
# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
# 丑数 就是质因子只包含 2、3 和 5 的正整数。
# 示例 1：
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
# 示例 2：
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
# 提示：
# 1 <= n <= 1690


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1] * n
        p2, p3, p5 = 0, 0, 0
        i = 1
        while i < n:
            if ans[p2] * 2 <= ans[p3] * 3 and ans[p2] * 2 <= ans[p5] * 5:
                ans[i] = ans[p2] * 2
                p2 += 1
            elif ans[p3] * 3 <= ans[p2] * 2 and ans[p3] * 3 <= ans[p5] * 5:
                ans[i] = ans[p3] * 3
                p3 += 1
            elif ans[p5] * 5 <= ans[p2] * 2 and ans[p5] * 5 <= ans[p3] * 3:
                ans[i] = ans[p5] * 5
                p5 += 1
            if ans[i] != ans[i - 1]:
                i += 1
        return ans[n - 1]