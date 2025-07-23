# 2025.07.23力扣网刷题
# 最大重复子字符串——字符串、动态规划、字符串匹配、第40场双周赛——简单
# 给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。
# 单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。
# 给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。
# 示例 1：
# 输入：sequence = "ababc", word = "ab"
# 输出：2
# 解释："abab" 是 "ababc" 的子字符串。
# 示例 2：
# 输入：sequence = "ababc", word = "ba"
# 输出：1
# 解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。
# 示例 3：
# 输入：sequence = "ababc", word = "ac"
# 输出：0
# 解释："ac" 不是 "ababc" 的子字符串。
# 提示：
# 1 <= sequence.length <= 100
# 1 <= word.length <= 100
# sequence 和 word 都只包含小写英文字母。

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        ans = 0
        n = len(sequence) // len(word)
        for i in range(1, n + 1):
            if sequence.find(word * i) != -1:
                ans = i
        return ans