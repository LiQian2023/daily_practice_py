# 2024.11.22力扣网刷题
# 统计不是特殊数字的数字数量——数组、数学、数论——中等
# 给你两个 正整数 l 和 r。对于任何数字 x，x 的所有正因数（除了 x 本身）被称为 x 的 真因数。
# 如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：
# 数字 4 是 特殊数字，因为它的真因数为 1 和 2。
# 数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
# 返回区间[l, r] 内 不是 特殊数字 的数字数量。
# 示例 1：
# 输入： l = 5, r = 7
# 输出： 3
# 解释：
# 区间[5, 7] 内不存在特殊数字。
# 示例 2：
# 输入： l = 4, r = 16
# 输出： 11
# 解释：
# 区间[4, 16] 内的特殊数字为 4 和 9。
# 提示：
# 1 <= l <= r <= 10^9

class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        n = int(r ** 0.5)
        isprime = [True] * (n + 1)
        prime = []
        primeSize = 0
        ans = r - l + 1
        for i in range(2, n + 1):
            if isprime[i]:
                prime.append(i)
                primeSize += 1
                if l <= i * i <= r:
                    ans -= 1
            for j in range(primeSize):
                if i * prime[j] > n:
                    break
                isprime[i * prime[j]] = False
                if i % prime[j] == 0:
                    break
        return ans
