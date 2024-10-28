# 2024.10.28力扣网刷题
# 找出第 K 个字符 I——位运算、递归、数学、模拟——简单
# Alice 和 Bob 正在玩一个游戏。最初，Alice 有一个字符串 word = "a"。
# 给定一个正整数 k。
# 现在 Bob 会要求 Alice 执行以下操作 无限次 :
# 将 word 中的每个字符 更改 为英文字母表中的 下一个 字符来生成一个新字符串，并将其 追加 到原始的 word。
# 例如，对 "c" 进行操作生成 "cd"，对 "zb" 进行操作生成 "zbac"。
# 在执行足够多的操作后， word 中 至少 存在 k 个字符，此时返回 word 中第 k 个字符的值。
# 注意，在操作中字符 'z' 可以变成 'a'。
# 示例 1:
# 输入：k = 5
# 输出："b"
# 解释：
# 最初，word = "a"。需要进行三次操作:
# 生成的字符串是 "b"，word 变为 "ab"。
# 生成的字符串是 "bc"，word 变为 "abbc"。
# 生成的字符串是 "bccd"，word 变为 "abbcbccd"。
# 示例 2 :
# 输入：k = 10
# 输出："c"
# 提示：
# 1 <= k <= 500


class Solution(object):
    def dfs(self, word, k):
        length = len(word)
        if length >= k:
            return word
        word_list = list(word)
        for i in range(length):
            word += chr(ord(word_list[i]) + 1)
        ret = Solution().dfs(word, k)
        return ret

    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        word = Solution().dfs('a', k)
        return word[k - 1]


print(Solution().kthCharacter(500))

