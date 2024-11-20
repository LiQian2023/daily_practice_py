# 2024.11.20力扣网刷题
# 二进制求和——位运算、数学、字符串、模拟——简单
# 给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
# 输入为 非空 字符串且只包含数字 1 和 0。
# 示例 1:
# 输入: a = "11", b = "10"
# 输出 : "101"
# 示例 2 :
# 输入 : a = "1010", b = "1011"
# 输出 : "10101"
# 提示：
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10 ^ 4
# 字符串如果不是 "0" ，就都不含前导零。
# 注意：本题与主站 67 题相同：https://leetcode-cn.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = int(a) + int(b)
        ans = list(str(ans))
        len1 = len(ans)
        for i in range(len1):
            ans[i] = int(ans[i])
        i = len1 - 1
        while i >= 0:
            if i and ans[i] > 1:
                ans[i - 1] += ans[i] // 2
                ans[i] %= 2
                i -= 1
            elif i == 0 and ans[i] > 1:
                ans.insert(i, ans[i] // 2)
                len1 += 1
                ans[i + 1] %= 2
            else:
                i -= 1
        for i in range(len1):
            ans[i] = str(ans[i])
        return ''.join(ans)


a = "111"
b = "1010"
print(Solution().addBinary(a, b))