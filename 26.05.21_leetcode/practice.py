# 2026.05.21力扣网刷题
# 面试题 05.07.配对交换——位运算——简单
# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位 0 与位 1 交换，位 2 与位 3 交换，以此类推）。
# 示例 1：
# 输入：num = 2（或者 0b10）
# 输出：1(或者 0b01)
# 示例 2：
# 输入：num = 3
# 输出：3
# 提示 :
# num 的范围在[0, 2^30 - 1]之间，不会发生整数溢出。

class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num1, num2 = 0x55555555, 0xaaaaaaaa
        odd, even = num & num2, num & num1
        odd >>= 1
        even <<= 1
        return odd ^ even