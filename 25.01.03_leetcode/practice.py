# 2025.01.03力扣网刷题
# 字符串的最大公因子——数学、字符串——简单
# 对于字符串 s 和 t，只有在 s = t + t + t + ... + t + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
# 给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。
# 示例 1：
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 示例 2：
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 示例 3：
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
# 提示：
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 由大写英文字母组成

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        # 找最长公因子
        length, i = 0, 0
        while i < len1 and i < len2:
            if str1[i] != str2[i]:
                return ""
            if len1 % (i + 1) == len2 % (i + 1) == 0:
                length = i + 1
            i += 1
        ans = str1[:length]
        # 判断该公因子是否为有效公因子
        def helper(str, ans, len1, len2):
            i, j = 0, 0
            while i < len1:
                if str[i] != ans[j]:
                    return False
                i += 1
                j = (j + 1) % len2
            return True
        flag1 = helper(str1, ans, len1, length)
        flag2 = helper(str2, ans, len2, length)
        if flag1 and flag2:
            return ans
        return ""
