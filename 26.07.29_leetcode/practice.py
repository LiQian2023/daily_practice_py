# 2026.07.29力扣网刷题
# 67. 二进制求和——位运算、数学、字符串、模拟——简单
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
# 示例 1：
# 输入 : a = "11", b = "1"
# 输出："100"
# 示例 2：
# 输入：a = "1010", b = "1011"
# 输出："10101"
# 提示：
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = list(str(int(a)+int(b)))
        size = len(res)
        for i in range(size - 2, -1, -1):
            num = int(res[i + 1])
            a, b = num // 2, num % 2
            res[i] = str(int(res[i]) + a)
            res[i + 1] = str(b)
        if int(res[0]) >= 2:
            res[0] = str(int(res[0]) % 2)
            res.insert(0, '1')
        return ''.join(res)