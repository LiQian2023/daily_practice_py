# 2025.01.06力扣网刷题
# 螺旋遍历二维数组——数组、矩阵、模拟——简单
# 给定一个二维数组 array，请返回「螺旋遍历」该数组的结果。
# 螺旋遍历：从左上角开始，按照 向右、向下、向左、向上 的顺序 依次 提取元素，然后再进入内部一层重复相同的步骤，直到提取完所有元素。
# 示例 1：
# 输入：array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]
# 示例 2：
# 输入：array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 限制：
# 0 <= array.length <= 100
# 0 <= array[i].length <= 100
# 注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

class Solution(object):
    def spiralArray(self, array):
        """
        :type array: List[List[int]]
        :rtype: List[int]
        """
        row = len(array)
        ans = []
        if row:
            col = len(array[0])
            size = row * col
            length, begin = 0, 0
            while length < size:
                i, j = begin, begin
                if j == col - begin - 1:
                    ans.append(array[i][j])
                    i += 1
                    length += 1
                # 向右
                while j < col - begin - 1 and length < size:
                    ans.append(array[i][j])
                    length += 1
                    j += 1
                if i == row - begin - 1:
                    ans.append(array[i][j])
                    length += 1
                # 向下
                while i < row - begin - 1 and length < size:
                    ans.append(array[i][j])
                    length += 1
                    i += 1
                # 向左
                while j > begin and length < size:
                    ans.append(array[i][j])
                    length += 1
                    j -= 1
                # 向上
                while i > begin and length < size:
                    ans.append(array[i][j])
                    length += 1
                    i -= 1
                begin += 1
        return ans
