# 2025.01.25力扣网刷题
# 查找共用字符——数组、哈希表、字符串——简单
# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。
# 示例 1：
# 输入：words = ["bella", "label", "roller"]
# 输出：["e", "l", "l"]
# 示例 2：
# 输入：words = ["cool", "lock", "cook"]
# 输出：["c", "o"]
# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 由小写英文字母组成

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        length = len(words)
        hash = [0] * 26
        for i in range(length):
            tmp = [0] * 26
            length2 = len(words[i])
            for j in range(length2):
                key = ord(words[i][j]) - 97
                tmp[key] += 1
            for j in range(26):
                if i == 0 or tmp[j] < hash[j]:
                    hash[j] = tmp[j]
        ans = []
        for i in range(26):
            while hash[i]:
                ans.append(chr(i + 97))
                hash[i] -= 1
        return ans