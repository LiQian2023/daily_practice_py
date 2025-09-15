# 2025.09.15力扣网刷题
# 面试题 01.06.字符串压缩——字符串、双指针——简单
# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
# 比如，字符串aabcccccaaa会变为a2b1c5a3。
# 若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。
# 示例 1：
# 输入："aabcccccaaa"
# 输出："a2b1c5a3"
# 示例 2：
# 输入："abbccd"
# 输出："abbccd"
# 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
# 提示：
# 字符串长度在[0, 50000] 范围内。

class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        length = len(S)
        if length == 0:
            return S
        l, r = 0, 0
        ans, ans_len = '', 0
        while r <= length:
            ans += S[l]
            while r < length and S[l] == S[r]:
                r += 1
            ans += str(r - l)
            l = r
            r += 1
        ans_len = len(ans)
        return ans if ans_len < length else S