# 2024.11.28力扣网刷题
# 三步问题——记忆化搜索、数学、动态规划——简单
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。
# 示例1 :
# 输入：n = 3
# 输出：4
# 说明 : 有四种走法
# 示例2 :
# 输入：n = 5
# 输出：13
# 提示 :
# n范围在[1, 1000000]之间

class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        MOD = 10**9+7
        step = [1, 1, 2, 4]
        for i in range(4, n + 1):
            step[0] = step[1] % MOD
            step[1] = step[2] % MOD
            step[2] = step[3] % MOD
            step[3] = ((step[0] + step[1]) % MOD + step[2]) % MOD
        return step[3]