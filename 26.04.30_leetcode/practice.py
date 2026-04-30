# 2026.04.30力扣网刷题
# 面试题 05.03.翻转数位——位运算、动态规划——简单
# 给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。
# 示例 1：
# 输入 : num = 1775(110111011112)
# 输出 : 8
# 示例 2：
# 输入 : num = 7(01112)
# 输出 : 4

class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = bin(num)[2:].split('0')
        if(num < 0):
            tmp =lambda n, bits=32: format(n & ((1 << bits) - 1), '0%db' % bits)
            num_list = tmp(num).split('0')
        dp = []
        for b in num_list:
            dp.append(len(b))
        ans = dp[0] + 1
        for i in range(1, len(dp)):
            ans = max(ans, dp[i - 1] + dp[i] + 1)
        return ans if ans < 32 else 32