# 2026.06.30力扣网刷题
# 1358. 包含所有三种字符的子字符串数目——资深工程师、哈希表、字符串、滑动串口、第20场双周赛——中等
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
# 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
# 示例 1：
# 输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
# 示例 2：
# 输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
# 示例 3：
# 输入：s = "abc"
# 输出：1
# 提示：
# 3 <= s.length <= 5 x 10 ^ 4
# s 只包含字符 a，b 和 c 。

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a, b, c, n, res = 0, 0, 0, len(s), 0
        l, r = 0, 0
        while r < n:
            if s[r] == 'a':
                a += 1
            elif s[r] == 'b':
                b += 1
            elif s[r] == 'c':
                c += 1
            while l <= r - 2 and a > 0 and b > 0 and c > 0:
                res += n - r
                if s[l] == 'a':
                    a -= 1
                elif s[l] == 'b':
                    b -= 1
                else:
                    c -= 1
                l += 1
            r += 1
        return res