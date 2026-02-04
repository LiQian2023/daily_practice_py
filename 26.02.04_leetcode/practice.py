# 2026.02.04力扣网刷题
# 最长回文子串——双指针、字符串、动态规划——中等
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 提示：
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        # 字符串拆分
        tmp = []
        for i in range(length):
            tmp.append(str(s[i]))
            if i < length - 1:
                tmp.append(',')
        # 记录最大子串
        max_mid = []
        tmp_size = len(tmp)
        for i in range(tmp_size):
            l = r = i
            while l >= 0 and r < tmp_size and tmp[l] == tmp[r]:
                l -= 1
                r += 1
            max_mid.append((r - l - 1) // 2)
        # 获取最大子串中点及半径
        longest, longest_i = max_mid[0], 0
        for i in range(tmp_size):
            if longest < max_mid[i]:
                longest = max_mid[i]
                longest_i = i
        # 记录中间最大子串
        ans = ""
        l, r = longest_i - longest, longest_i + longest
        while l <= r:
            if tmp[l] != ',':
                ans += tmp[l]
            l += 1
        ans_size = len(ans)
        # 找边界最大值
        l, r = 0, length - 1
        while l < length and r >= 0:
            if s[l] == s[0]:
                l += 1
            if s[r] == s[-1]:
                r -= 1
            if (l < length and s[l] != s[0]) and (r >= 0 and s[r] != s[-1]):
                break
        r += 1
        max_left, max_right = l, length - r
        # 处理边界
        if ans_size < max_left:
            ans = ''
            for i in range(max_left):
                ans += s[i]
            ans_size = max_left
        if ans_size < max_right:
            ans = ""
            for i in range(r, length):
                ans += s[i]
        return ans

