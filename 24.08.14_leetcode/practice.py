# 2024.08.14力扣网刷题
# 按奇偶性交换后的最大数字——排序、堆（优先队列）——简单
# 给你一个正整数 num 。你可以交换 num 中 奇偶性 相同的任意两位数字（即，都是奇数或者偶数）。
# 返回交换 任意 次之后 num 的 最大 可能值。
# 示例 1：
# 输入：num = 1234
# 输出：3412
# 解释：交换数字 3 和数字 1 ，结果得到 3214 。
# 交换数字 2 和数字 4 ，结果得到 3412 。
# 注意，可能存在其他交换序列，但是可以证明 3412 是最大可能值。
# 注意，不能交换数字 4 和数字 1 ，因为它们奇偶性不同。
# 示例 2：
# 输入：num = 65875
# 输出：87655
# 解释：交换数字 8 和数字 6 ，结果得到 85675 。
# 交换数字 5 和数字 7 ，结果得到 87655 。
# 注意，可能存在其他交换序列，但是可以证明 87655 是最大可能值。
# 提示：
# 1 <= num <= 10^9

class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for i in range(len(num)):
            num[i] = int(num[i])
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if num[j] > num[i] and num[i] % 2 == num[j] % 2:
                    num[i], num[j] = num[j], num[i]
        ans = 0
        for i in range(len(num)):
            ans *= 10
            ans += num[i]
        return ans

num = 1234
print(Solution().largestInteger(num))