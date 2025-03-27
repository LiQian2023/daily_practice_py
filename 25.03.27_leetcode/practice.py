# 2025.03.27力扣网刷题
# 回文排列——位运算、哈希表、字符串——简单
# 给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。
# 回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。
# 回文串不一定是字典当中的单词。
# 示例1：
# 输入："tactcoa"
# 输出：true（排列有"tacocat"、"atcocta"，等等）

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash = [0] * 256
        length = len(s)
        for i in range(length):
            key = ord(s[i])
            hash[key] += 1
        ans = 0
        for i in range(256):
            if hash[i] % 2:
                ans += 1
        return ans == 0 or ans == 1