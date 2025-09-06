# 2025.09.06力扣网刷题
# 十六进制和三十六进制转化——数学、字符串、第160场双周赛——简单
# 给你一个整数 n。
# 返回 n^2 的 十六进制表示 和 n^3 的 三十六进制表示 拼接成的字符串。
# 十六进制 数定义为使用数字 0 – 9 和大写字母 A - F 表示 0 到 15 的值。
# 三十六进制 数定义为使用数字 0 – 9 和大写字母 A - Z 表示 0 到 35 的值。
# 示例 1：
# 输入：n = 13
# 输出： "A91P1"
# 解释：
# n2 = 13 * 13 = 169。在十六进制中，它转换为(10 * 16) + 9 = 169，对应于 "A9"。
# n3 = 13 * 13 * 13 = 2197。在三十六进制中，它转换为(1 * 362) + (25 * 36) + 1 = 2197，对应于 "1P1"。
# 连接两个结果得到 "A9" + "1P1" = "A91P1"。
# 示例 2：
# 输入：n = 36
# 输出："5101000"
# 解释：
# n2 = 36 * 36 = 1296。在十六进制中，它转换为(5 * 162) + (1 * 16) + 0 = 1296，对应于 "510"。
# n3 = 36 * 36 * 36 = 46656。在三十六进制中，它转换为(1 * 363) + (0 * 362) + (0 * 36) + 0 = 46656，对应于 "1000"。
# 连接两个结果得到 "510" + "1000" = "5101000"。
# 提示 :
# 1 <= n <= 1000

class Solution(object):
    def concatHex36_(self, n):
        """
        :type n: int
        :rtype: str
        """
        hash = []
        for i in range(36):
            if i < 10:
                hash.append(str(i))
            else:
                ch = chr(i - 10 + ord('A'))
                hash.append(ch)
        pre = n ** 2
        suf = n ** 3
        ans = []
        while suf:
            key = suf % 36
            ans.append(hash[key])
            suf //= 36
        while pre:
            key = pre % 16
            ans.append(hash[key])
            pre //= 16
        ans.reverse()
        return ''.join(ans)

    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        def Transform(ans, num, adv):
            while num:
                key = num % adv
                num //= adv
                if key < 10:
                    ans.append(str(key))
                else:
                    ch = chr(key - 10 + ord('A'))
                    ans.append(ch)
            return ans
        ans = []
        pre, suf = n ** 2, n ** 3
        ans = Transform(ans, suf, 36)
        ans = Transform(ans, pre, 16)
        ans.reverse()
        return ''.join(ans)