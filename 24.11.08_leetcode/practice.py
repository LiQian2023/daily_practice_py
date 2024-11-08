# 2024.11.08力扣网刷题
# 字符串中的最大奇数——贪心、数学、字符串——简单
# 给你一个字符串 num ，表示一个大整数。请你在字符串 num 的所有 非空子字符串 中找出 值最大的奇数 ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 "" 。
# 子字符串 是字符串中的一个连续的字符序列。
# 示例 1：
# 输入：num = "52"
# 输出："5"
# 解释：非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。
# 示例 2：
# 输入：num = "4206"
# 输出：""
# 解释：在 "4206" 中不存在奇数。
# 示例 3：
# 输入：num = "35427"
# 输出："35427"
# 解释："35427" 本身就是一个奇数。
# 提示：
# 1 <= num.length <= 10^5
# num 仅由数字组成且不含前导零


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        num = list(num)
        length = len(num)
        for i in range(length - 1, -1, -1):
            if int(num[i]) % 2:
                break
            num.pop(i)
        return ''.join(num)