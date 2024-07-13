# 2024.07.14力扣网刷题
# 计数二进制子串——双指针、字符串——简单
# 给定一个字符串 s，统计并返回具有相同数量 0 和 1 的非空（连续）子字符串的数量，
# 并且这些子字符串中的所有 0 和所有 1 都是成组连续的。
# 重复出现（不同位置）的子串也要统计它们出现的次数。
# 示例 1：
# 输入：s = "00110011"
# 输出：6
# 解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
# 注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
# 另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。
# 示例 2：
# 输入：s = "10101"
# 输出：4
# 解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。
# 提示：
# 1 <= s.length <= 10^5
# s[i] 为 '0' 或 '1'

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        one, zero, ans, i, flag = 0, 0, 0, 0, 0
        length = len(s)
        while i < length:
            # 统计'0'的数量
            while i < length and s[i] == '0':
                i += 1
                zero += 1
            if zero:
                flag += 1
            if flag == 2:
                ans += min(zero, one)
                one = 0
                flag -= 1
            # 统计'1'的数量
            while i < length and s[i] == '1':
                i += 1
                one += 1
            if one:
                flag += 1
            if flag == 2:
                ans += min(zero, one)
                zero = 0
                flag -= 1
        return ans


s = ('00110011')
print(Solution().countBinarySubstrings(s))
