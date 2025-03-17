# 2025.03.17力扣网刷题
# 奇偶频次间的最大差值 I——哈希表、字符串、计数——简单
# 给你一个由小写英文字母组成的字符串 s 。请你找出字符串中两个字符的出现频次之间的 最大 差值，这两个字符需要满足：
# 一个字符在字符串中出现 偶数次 。
# 另一个字符在字符串中出现 奇数次 。
# 返回 最大 差值，计算方法是出现 奇数次 字符的次数 减去 出现 偶数次 字符的次数。
# 示例 1：
# 输入：s = "aaaaabbc"
# 输出：3
# 解释：
# 字符 'a' 出现 奇数次 ，次数为 5 ；字符 'b' 出现 偶数次 ，次数为 2 。
# 最大差值为 5 - 2 = 3 。
# 示例 2：
# 输入：s = "abcabcab"
# 输出：1
# 解释：
# 字符 'a' 出现 奇数次 ，次数为 3 ；字符 'c' 出现 偶数次 ，次数为 2 。
# 最大差值为 3 - 2 = 1 。
# 提示：
# 3 <= s.length <= 100
# s 仅由小写英文字母组成。
# s 至少由一个出现奇数次的字符和一个出现偶数次的字符组成。

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        even, odd = 0, 0
        length = len(s)
        hash = [0] * 26
        for i in range(length):
            hash[ord(s[i]) - ord('a')] += 1
        for i in range(26):
            if hash[i] and hash[i] % 2 == 0:
                if even == 0 or hash[i] < even:
                    even = hash[i]
            else:
                if hash[i] > odd:
                    odd = hash[i]
        return odd - even

if __name__ == '__main__':
    s = Solution()
    print(s.maxDifference("aaaaabbc"))
    print(s.maxDifference("abcabcab"))