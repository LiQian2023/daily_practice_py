# 2024.07.05力扣网刷题
# 修改矩阵——数组、矩阵——简单
# 给你一个下标从 0 开始、大小为 m x n 的整数矩阵 matrix ，新建一个下标从 0 开始、名为 answer 的矩阵。
# 使 answer 与 matrix 相等，接着将其中每个值为 - 1 的元素替换为所在列的 最大 元素。
# 返回矩阵 answer 。
# 示例 1：
# 输入：matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
# 输出： [[1, 2, 9], [4, 8, 6], [7, 8, 9]]
# 解释：上图显示了发生替换的元素（蓝色区域）。
# - 将单元格[1][1] 中的值替换为列 1 中的最大值 8 。
# - 将单元格[0][2] 中的值替换为列 2 中的最大值 9 。
# 示例 2：
# 输入：matrix = [[3, -1], [5, 2]]
# 输出： [[3, 2], [5, 2]]
# 解释：上图显示了发生替换的元素（蓝色区域）。
# 提示：
# m == matrix.length
# n == matrix[i].length
# 2 <= m, n <= 50
# - 1 <= matrix[i][j] <= 100
# 测试用例中生成的输入满足每列至少包含一个非负整数。

class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        # 复制元素
        for i in range(len(matrix)):
            ans_i = []
            for j in range(len(matrix[i])):
                ans_i.append(matrix[i][j])
            ans.append(ans_i)
        # 修改矩阵
        for i in range(len(ans[0])):
            flag = []
            max = ans[0][i]
            for j in range(len(ans)):
                if ans[j][i] == -1:
                    flag.append(j)
                elif ans[j][i] > max:
                    max = ans[j][i]
            for z in flag:
                ans[z][i] = max
        return ans


matrix = [[1, 2, -1], [4, -1, 6], [7, 8, 9]]
print(Solution().modifiedMatrix(matrix))