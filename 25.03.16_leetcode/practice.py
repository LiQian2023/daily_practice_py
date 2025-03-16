# 2025.03.16力扣网刷题
# 每个字符最多出现两次的最长子字符串——哈希表、字符串、滑动窗口——简单
# 给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。
# 示例 1：
# 输入： s = "bcbbbcba"
# 输出： 4
# 解释：
# 以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
# 示例 2：
# 输入： s = "aaaa"
# 输出： 2
# 解释：
# 以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
# 提示：
# 2 <= s.length <= 100
# s 仅由小写英文字母组成。

class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = [0] * 26
        len1 = len(s)
        l, r = 0, 0
        ans = 0
        while r < len1:
            key1 = ord(s[r]) - ord('a')
            hash[key1] += 1
            while hash[key1] > 2:
                key2 = ord(s[l]) - ord('a')
                hash[key2] -= 1
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
            r += 1
        return ans