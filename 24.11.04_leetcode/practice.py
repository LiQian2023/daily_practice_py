# 2024.11.04力扣网刷题
# 平方数之和——数学、双指针、二分查找——中等
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
# 示例 1：
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
# 示例 2：
# 输入：c = 3
# 输出：false
# 提示：
# 0 <= c <= 2^31 - 1


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(pow(c / 2, 0.5)) + 1):
            b = c - pow(a, 2)
            x = int(pow(b, 0.5))
            if b == pow(x, 2):
                return True
        return False
