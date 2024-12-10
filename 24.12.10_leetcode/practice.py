# 2024.12.10力扣网刷题
# 统计对称整数的数目——数学、枚举——简单
# 给你两个正整数 low 和 high 。
# 对于一个由 2 * n 位数字组成的整数 x ，如果其前 n 位数字之和与后 n 位数字之和相等，则认为这个数字是一个对称整数。
# 返回在[low, high] 范围内的 对称整数的数目 。
# 示例 1：
# 输入：low = 1, high = 100
# 输出：9
# 解释：在 1 到 100 范围内共有 9 个对称整数：11、22、33、44、55、66、77、88 和 99 。
# 示例 2：
# 输入：low = 1200, high = 1230
# 输出：4
# 解释：在 1200 到 1230 范围内共有 4 个对称整数：1203、1212、1221 和 1230 。
# 提示：
# 1 <= low <= high <= 10^4

class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        for i in range(low, high + 1):
            if i < 10:
                i = 10
                continue
            elif 100 <= i <= 999:
                i = 1000
                continue
            elif 10 <= i <= 99:
                if i % 10 == i // 10:
                    ans += 1
            elif 1000 <= i <= 10000:
                a = i % 100
                b = i // 100
                if a%10 + a//10 == b%10 + b//10:
                    ans += 1
        return ans