# 2024.07.04力扣网刷题
# 验证回文串 II——贪心、双指针、字符串——简单
# 给你一个字符串 s，最多 可以从中删除一个字符。
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：s = "aba"
# 输出：true
# 示例 2：
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。
# 示例 3：
# 输入：s = "abc"
# 输出：false
# 提示：
# 1 <= s.length <= 10^5
# s 由小写英文字母组成

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        l = 0
        r = s_len - 1
        one = 1
        # 判断原字符串是否回文
        while l < r:
            if s[l] != s[r]:
                one -= 1
                break
            l += 1
            r -= 1
        if l >= r:
            return True
        # 删除左侧字符后判断是否回文
        i = l + 1
        j = r
        while i < j:
            if s[i] != s[j]:
                one -= 1
                break
            i += 1
            j -= 1
        # 删除右侧字符后判断是否回文
        i = l
        j = r - 1
        while i < j:
            if s[i] != s[j]:
                one -= 1
                break
            i += 1
            j -= 1
        return one != -2
