# 2025.02.28力扣网刷题
# 统计字符串中的元音子字符串——哈希表、字符串——简单
# 子字符串 是字符串中的一个连续（非空）的字符序列。
# 元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。
# 给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。
# 示例 1：
# 输入：word = "aeiouu"
# 输出：2
# 解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
# - "aeiouu"
# - "aeiouu"
# 示例 2：
# 输入：word = "unicornarihan"
# 输出：0
# 解释：word 中不含 5 种元音，所以也不会存在元音子字符串。
# 示例 3：
# 输入：word = "cuaieuouac"
# 输出：7
# 解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# 示例 4：
# 输入：word = "bbaeixoubb"
# 输出：0
# 解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。
# 提示：
# 1 <= word.length <= 100
# word 仅由小写英文字母组成

class Solution(object):
    def SearchSubstring(self, word, begin, end):
        hash = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        i = begin
        n = 0
        while i < end:
            if hash[word[i]] == 0:
                hash[word[i]] = 1
                n += 1
            if n == 5:
                break
            i += 1
        return 0 if n < 5 else end - i

    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        len1 = len(word)
        ans = 0
        i = 0
        while i < len1:
            if word[i] in "aeiou":
                j = i + 1
                while j <= len1:
                    if j == len1 or word[j] not in "aeiou":
                        if j - i < 5:
                            i = j
                            break
                        else:
                            ans += self.SearchSubstring(word, i, j)
                            break
                    j += 1
            i += 1
        return ans

        # 1.暴力法
        # count = 0
        # for i in range(len(word)):
        #     for j in range(i+1, len(word)+1):
        #         if self.isVowel(word[i:j]):
        #             count += 1
        # return count
        # 2.哈希表
        # count = 0
        # vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        # for i in range(len(word)):
        #     for j in range(i+1, len(word)+1):
        #         if self.isVowel(word[i:j]):
        #             for k in word[i:j]:
        #                 vowel[k] += 1
        #             if vowel['a'] > 0 and vowel['e'] > 0 and vowel['i'] > 0 and vowel['o'] > 0 and vowel['u'] > 0:
        #                 count += 1
        #             for k in word[i:j]:
        #                 vowel[k] -= 1
        # return count
        # 3.字符串
    #     count = 0
    #     for letter in word:
    #         if letter not in 'aeiouAEIOU':
    #             count += 1
    #     return count
    # def isVowel(self, word):
    #     vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    #     for i in word:
    #         if i in vowel:
    #             vowel[i] += 1
    #     if vowel['a'] > 0 and vowel['e'] > 0 and vowel['i'] > 0 and vowel['o'] > 0 and vowel['u'] > 0:
    #         return True
    #     else:
    #         return False



