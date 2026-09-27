# 2026.09.27力扣网刷题
# 1190. 反转每对括号间的子串——高级工程师、栈、字符串、括号序列、第154场周赛——中等
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。
# 示例 1：
# 输入：s = "(abcd)"
# 输出："dcba"
# 示例 2：
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 解释：先反转子字符串 "love" ，然后反转整个字符串。
# 示例 3：
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。
# 提示：
# 1 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 题目测试用例确保所有括号都是成对出现的

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, n = [], len(s)
        pair = [-1] * n
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                left = stack.pop()
                right = i
                pair[left] = right
                pair[right] = left
        ans = []
        i, j, step = 0, 0, 1
        while 0 <= i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                step = -step
            else:
                ans.append(s[i])
            i += step
        return ''.join(ans)