# 2024.11.17力扣网刷题
# 不用加号的加法——位运算、数学——简单
# 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。
# 示例 :
# 输入: a = 1, b = 1
# 输出 : 2
# 提示：
# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数

MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a %= MASK1
        b %= MASK1
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a

