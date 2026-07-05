# 2026.07.05力扣网刷题
# 3. 无重复字符的最长子串——中级工程师、哈希表、字符串、滑动窗口——中等
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出 : 3
# 解释 : 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2 :
# 输入 : s = "bbbbb"
# 输出 : 1
# 解释 : 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3 :
# 输入 : s = "pwwkew"
# 输出 : 3
# 解释 : 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 提示：
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [0] * 128
        ans = 0
        l, r, n = 0, 0, len(s)
        while r < n:
            rindex = ord(s[r])
            hash[rindex] += 1
            while hash[rindex] > 1:
                lindex = ord(s[l])
                hash[lindex] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans