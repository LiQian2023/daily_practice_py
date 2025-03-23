# 2025.03.23力扣网刷题
# 判断一个括号字符串是否有效——栈、贪心、字符串——中等
# 一个括号字符串是只由 '(' 和 ')' 组成的 非空 字符串。如果一个字符串满足下面 任意 一个条件，那么它就是有效的：
# 字符串为().
# 它可以表示为 AB（A 与 B 连接），其中A 和 B 都是有效括号字符串。
# 它可以表示为(A) ，其中 A 是一个有效括号字符串。
# 给你一个括号字符串 s 和一个字符串 locked ，两者长度都为 n 。locked 是一个二进制字符串，只包含 '0' 和 '1' 。对于 locked 中 每一个 下标 i ：
# 如果 locked[i] 是 '1' ，你 不能 改变 s[i] 。
# 如果 locked[i] 是 '0' ，你 可以 将 s[i] 变为 '(' 或者 ')' 。
# 如果你可以将 s 变为有效括号字符串，请你返回 true ，否则返回 false 。
# 示例 1：
# 输入：s = "))()))", locked = "010100"
# 输出：true
# 解释：locked[1] == '1' 和 locked[3] == '1' ，所以我们无法改变 s[1] 或者 s[3] 。
# 我们可以将 s[0] 和 s[4] 变为 '(' ，不改变 s[2] 和 s[5] ，使 s 变为有效字符串。
# 示例 2：
# 输入：s = "()()", locked = "0000"
# 输出：true
# 解释：我们不需要做任何改变，因为 s 已经是有效字符串了。
# 示例 3：
# 输入：s = ")", locked = "0"
# 输出：false
# 解释：locked 允许改变 s[0] 。
# 但无论将 s[0] 变为 '(' 或者 ')' 都无法使 s 变为有效字符串。
# 示例 4：
# 输入：s = "(((())(((())", locked = "111111010111"
# 输出：true
# 解释：locked 允许我们改变 s[6] 和 s[8]。
# 我们将 s[6] 和 s[8] 改为 ')' 使 s 变为有效字符串。
# 提示：
# n == s.length == locked.length
# 1 <= n <= 10^5
# s[i] 要么是 '(' 要么是 ')' 。
# locked[i] 要么是 '0' 要么是 '1' 。

class Solution(object):
    def canBeValid1(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        len1 = len(s)
        stack1 = []     # 不可变字符栈
        top1 = 0
        stack2 = []     # 可变字符栈
        top2 = 0
        for i in range(len1):
            if locked[i] == '1':
                # 非空栈，并且匹配成功，执行出栈操作
                if top1 and s[i] == ')' and s[stack1[top1-1]] == '(':
                    stack1.pop()
                    top1 -= 1
                # 空栈，或者匹配失败，入栈
                else:
                    stack1.append(i)
                    top1 += 1
            else:
                stack2.append(i)
                top2 += 1
        n = 0
        while top1 and top2:
            key1 = stack1[top1 - 1]
            key2 = stack2[top2 - 1]
            # 匹配成功，出栈
            if (s[key1] == ')' and key2 < key1) or (s[key1] == '(' and key2 > key1):
                stack1.pop()
                top1 -= 1
            # 匹配失败，记录字符数量
            else:
                n += 1
            stack2.pop()
            top2 -= 1
        n += top2
        return top1 == 0 and n % 2 == 0

    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        len1 = len(s)
        # top1：全部未匹配，top2：全部匹配
        top1, top2 = 0, 0
        for i in range(len1):
            # 不可变字符
            if locked[i] == '1':
                diff = 0    # 括号值：左括号，长度增加，右括号，长度减少
                # 左括号
                if s[i] == '(':
                    diff = 1
                else:
                    diff = -1
                top1 += diff    # 改变子串最长未匹配长度
                top2 = max(top2 + diff, (i + 1) % 2)    # 子串全部完成匹配的最大长度
            # 可变字符
            else:
                top1 += 1   # 默认可变字符为左括号
                top2 = max(top2 - 1, (i + 1) % 2)
            # 当未匹配的长度小于完成匹配的最大长度时，说明此时的子串中存在无法匹配的字符
            if top1 < top2:
                return False
        # top2 == 0 表示字符串全部完成匹配，否则存在无法匹配的字符
        return top2 == 0


if __name__ == '__main__':
    s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
    locked = "100011110110011011010111100111011101111110000101001101001111"
    print(Solution().canBeValid(s, locked))

