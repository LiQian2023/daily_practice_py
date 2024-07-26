# 2024.07.26力扣网刷题
# 距离顺序排列矩阵单元格——几何、数学、数组、矩阵、排序——简单
# 给定四个整数 rows, cols, rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是(rCenter, cCenter) 。
# 返回矩阵中的所有单元格的坐标，并按与(rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。
# 单元格(r1, c1) 和(r2, c2) 之间的距离为 | r1 - r2 | +| c1 - c2 | 。
# 示例 1：
# 输入：rows = 1, cols = 2, rCenter = 0, cCenter = 0
# 输出： [[0, 0], [0, 1]]
# 解释：从(r0, c0) 到其他单元格的距离为：[0, 1]
# 示例 2：
# 输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1
# 输出： [[0, 1], [0, 0], [1, 1], [1, 0]]
# 解释：从(r0, c0) 到其他单元格的距离为：[0, 1, 1, 2]
# [[0, 1], [1, 1], [0, 0], [1, 0]] 也会被视作正确答案。
# 示例 3：
# 输入：rows = 2, cols = 3, rCenter = 1, cCenter = 2
# 输出： [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
# 解释：从(r0, c0) 到其他单元格的距离为：[0, 1, 1, 2, 2, 3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1, 2], [1, 1], [0, 2], [1, 0], [0, 1], [0, 0]] 。
# 提示：
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols


class Solution(object):
    def allCellsDistOrder1(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        ans = [[rCenter, cCenter]]
        print(ans)
        for i in range(rows):
            for j in range(cols):
                z = 0
                while z < len(ans):
                    dx1 = abs(i - rCenter) + abs(j - cCenter)
                    dx2 = abs(ans[z][0] - rCenter) + abs(ans[z][1] - cCenter)
                    if dx1 < dx2:
                        ans.insert(z, [i, j])
                        break
                    z += 1
                if z == len(ans):
                    ans.append([i, j])
        ans.pop(0)
        print(ans)
        return ans

    def takeThird(self, ans):
        return ans[2]

    def allCellsDistOrder2(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        ans = [[rCenter, cCenter, 0]]
        print(ans)
        for i in range(rows):
            for j in range(cols):
                dx = abs(i - rCenter) + abs(j - cCenter)
                ans.append([i, j, dx])
        ans.sort(key=Solution().takeThird)
        ans.pop(0)
        for i in range(len(ans)):
            ans[i].pop(2)
        print(ans)
        return ans

    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        ret = [(i,j) for i in range(rows) for j in range(cols)]
        ret.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return ret


rows, cols, rCenter, cCenter = 2, 2, 1, 2
print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))
