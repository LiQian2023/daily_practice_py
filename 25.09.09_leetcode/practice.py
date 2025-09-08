# 2025.09.09力扣网刷题
# 验证回文串——双指针、字符串——简单
# 给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。
# 本题中，将空字符串定义为有效的 回文串 。
# 示例 1：
# 输入 : s = "A man, a plan, a canal: Panama"
# 输出 : true
# 解释："amanaplanacanalpanama" 是回文串
# 示例 2：
# 输入 : s = "race a car"
# 输出 : false
# 解释："raceacar" 不是回文串
# 提示：
# 1 <= s.length <= 2 * 105
# 字符串 s 由 ASCII 字符组成
# 注意：本题与主站 125 题相同： https ://leetcode-cn.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        length = len(s)
        l, r = 0, length - 1
        while l < r:
            while l < length and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l < r and s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True