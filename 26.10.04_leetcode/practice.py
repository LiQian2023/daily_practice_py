# 2026.10.04力扣网刷题
# 678. 有效的括号字符串——栈、贪心、字符串、动态规划、括号序列——中等
# 给你一个只包含三种字符的字符串，支持的字符类型分别是 '('、')' 和 '*'。请你检验这个字符串是否为有效字符串，如果是 有效 字符串返回 true 。
# 有效 字符串符合如下规则：
# 任何左括号 '(' 必须有相应的右括号 ')'。
# 任何右括号 ')' 必须有相应的左括号 '(' 。
# 左括号 '(' 必须在对应的右括号之前 ')'。
# '*' 可以被视为单个右括号 ')' ，或单个左括号 '(' ，或一个空字符串 ""。
# 示例 1：
# 输入：s = "()"
# 输出：true
# 示例 2：
# 输入：s = "(*)"
# 输出：true
# 示例 3：
# 输入：s = "(*))"
# 输出：true
# 提示：
# 1 <= s.length <= 100
# s[i] 为 '('、')' 或 '*'

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1, stack2 = [], []
        ans = True
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            elif s[i] == ')':
                len1, len2 = len(stack1), len(stack2)
                if len1:
                    stack1.pop()
                elif len2:
                    stack2.pop()
                elif len1 == 0 and len2 == 0:
                    ans = False
                    break
            else:
                stack2.append(i)
        if ans:
            len1, len2 = len(stack1), len(stack2)
            if len1 > len2:
                ans = False
            else:
                i, j = 0, 0
                while i < len1 and j < len2:
                    if stack1[i] < stack2[j]:
                        i += 1
                    j += 1
                if i < len1:
                    ans = False
        return ans