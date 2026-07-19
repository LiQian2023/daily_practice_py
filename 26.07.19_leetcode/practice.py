# 2026.07.19力扣网刷题
# 1081. 不同字符的最小子序列——高级专家、栈、贪心、字符串、单调栈、第140场周赛——中等
# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
# 示例 1：
# 输入：s = "bcabc"
# 输出："abc"
# 示例 2：
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 提示：
# 1 <= s.length <= 1000
# s 由小写英文字母组成
# 注意：该题与 316 https://leetcode.cn/problems/remove-duplicate-letters/ 相同

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last, hash = [0] * 26, [-1] * 26
        n = len(s)
        for i in range(n):
            key = ord(s[i]) - ord('a')
            last[key] = i
        ans = []
        top = -1
        for i in range(n):
            key = ord(s[i]) - ord('a')
            if hash[key] != -1:
                continue
            while top >= 0 and ans[top] > s[i] and last[ord(ans[top]) - ord('a')] > i:
                hash[ord(ans[top]) - ord('a')] = -1
                ans.pop()
                top -= 1
            ans.append(s[i])
            top += 1
            hash[key] = i
        return ''.join(ans)