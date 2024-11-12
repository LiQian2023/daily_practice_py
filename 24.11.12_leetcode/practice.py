# 2024.11.12力扣网刷题
# 统计满足 K 约束的子字符串数量 I——字符串、滑动窗口——简单
# 给你一个 二进制 字符串 s 和一个整数 k。
# 如果一个 二进制字符串 满足以下任一条件，则认为该字符串满足 k 约束：
# 字符串中 0 的数量最多为 k。
# 字符串中 1 的数量最多为 k。
# 返回一个整数，表示 s 的所有满足 k 约束 的子字符串的数量。
# 示例 1：
# 输入：s = "10101", k = 1
# 输出：12
# 解释：
# s 的所有子字符串中，除了 "1010"、"10101" 和 "0101" 外，其余子字符串都满足 k 约束。
# 示例 2：
# 输入：s = "1010101", k = 2
# 输出：25
# 解释：
# s 的所有子字符串中，除了长度大于 5 的子字符串外，其余子字符串都满足 k 约束。
# 示例 3：
# 输入：s = "11111", k = 1
# 输出：15
# 解释：
# s 的所有子字符串都满足 k 约束。
# 提示：
# 1 <= s.length <= 50
# 1 <= k <= s.length
# s[i] 是 '0' 或 '1'。

class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s = list(s)
        size = len(s)
        ans = 0
        l, r = 0, 0
        zero, one = 0, 0
        flag = True
        while l < size:
            if flag and r < size:
                if s[r] == '0':
                    zero += 1
                else:
                    one += 1
            if (zero > k and one > k) or r == size:
                ans += r - l
                if s[l] == '0':
                    zero -= 1
                else:
                    one -= 1
                l += 1
                flag = False
            if r < size and (zero <= k or one <= k):
                r += 1
                flag = True
        return ans


s = "10101"
k = 1
print(Solution().countKConstraintSubstrings(s,k))
