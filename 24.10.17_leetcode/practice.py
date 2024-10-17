# 2024.10.17力扣网刷题
# 通过删除字母匹配到字典里最长单词——数字、双指针、字符串、排序——中等
# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
# 示例 1：
# 输入：s = "abpcplea", dictionary = ["ale", "apple", "monkey", "plea"]
# 输出："apple"
# 示例 2：
# 输入：s = "abpcplea", dictionary = ["a", "b", "c"]
# 输出："a"
# 提示：
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s 和 dictionary[i] 仅由小写英文字母组成

class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary.sort()
        dictionary.sort(key=lambda x: len(x), reverse=True)
        len1 = len(s)
        for word in dictionary:
            i, j = 0, 0
            len2 = len(word)
            while i < len1 and j < len2:
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len2:
                return word
        return ""


s = "abce"
dictionary = ["abe","abc"]
print(Solution().findLongestWord(s,dictionary))