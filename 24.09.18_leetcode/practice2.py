# 2024.09.18力扣网刷题——2024.01.01C语言解答
# 有效的字母异位词——哈希表、字符串、排序——简单
# 给定两个字符串s和t ，编写一个函数来判断t是否是s的字母异位词。
# 示例
# 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例
# 2:
# 输入: s = "rat", t = "car"
# 输出: false
# 提示:
# 1 <= s.length, t.length <= 5 * 104
# s和t仅包含小写字母
# 进阶: 如果输入字符串包含unicode字符怎么办？你能否调整你的解法来应对这种情况？

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        return list1 == list2