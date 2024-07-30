# 2024.07.30力扣网刷题
# 双模幂运算——数组、数学、模拟——中等
# 给你一个下标从 0 开始的二维数组 variables ，其中 variables[i] = [ai, bi, ci, mi]，以及一个整数 target 。
# 如果满足以下公式，则下标 i 是 好下标：
# 0 <= i < variables.length
# ((ai^bi % 10)^ci) % mi == target
# 返回一个由 好下标 组成的数组，顺序不限 。
# 示例 1：
# 输入：variables = [[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target = 2
# 输出：[0, 2]
# 解释：对于 variables 数组中的每个下标 i ：
# 1) 对于下标 0 ，variables[0] = [2, 3, 3, 10] ，(2^3 % 10)^3 % 10 = 2 。
# 2) 对于下标 1 ，variables[1] = [3, 3, 3, 1] ，(3^3 % 10)^3 % 1 = 0 。
# 3) 对于下标 2 ，variables[2] = [6, 1, 1, 4] ，(6^1 % 10)^1 % 4 = 2 。
# 因此，返回[0, 2] 作为答案。
# 示例 2：
# 输入：variables = [[39, 3, 1000, 1000]], target = 17
# 输出：[]
# 解释：对于 variables 数组中的每个下标 i ：
# 1) 对于下标 0 ，variables[0] = [39, 3, 1000, 1000] ，(393 % 10)1000 % 1000 = 1 。
# 因此，返回[] 作为答案。
# 提示：
# 1 <= variables.length <= 100
# variables[i] == [ai, bi, ci, mi]
# 1 <= ai, bi, ci, mi <= 10^3
# 0 <= target <= 10^3


class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        # 模拟
        ans = []
        for i in range(len(variables)):
            num1 = ((variables[i][0] % 10) ** variables[i][1]) % 10
            num2 = ((num1 % variables[i][3]) ** variables[i][2]) % variables[i][3]
            if num2 == target:
                ans.append(i)
        return ans

    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        # pow方法
        ans = []
        for i in range(len(variables)):
            if pow(pow(variables[i][0], variables[i][1], 10),  variables[i][2], variables[i][3]) == target:
                ans.append(i)
        return ans


print(10.2 % 10)
