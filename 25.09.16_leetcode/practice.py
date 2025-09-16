# 2025.09.16力扣网刷题
# 面试题 01.09.字符串轮转——字符串、字符串匹配——简单
# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
# 示例 1：
# 输入：s1 = "waterbottle", s2 = "erbottlewat"
# 输出：True
# 示例 2：
# 输入：s1 = "aa", s2 = "aba"
# 输出：False
# 提示：
# 字符串长度在[0, 100000]范围内。
# 说明 :
# 你能只调用一次检查子串的方法吗？

class Solution(object):
    def isFlipedString1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        if length == 0:
            return True
        for k in range(length):
            sub = s1[k::] + s1[:k]
            if sub == s2:
                return True
        return False

    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        return (s1 + s1).find(s2) != -1