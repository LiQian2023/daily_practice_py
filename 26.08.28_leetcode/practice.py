# 2026.08.28力扣网刷题
# 3996. 偶数次骑士移动——中级工程师、数组、数学、第511场周赛——简单
# 给你两个整数数组 start 和 target，每个数组的形式均为[x, y]，表示标准 8 x 8 国际象棋棋盘上的一个格子。
# 如果骑士可以用 偶数 次移动从 start 到达 target，则返回 true；否则返回 false。
# 注意：骑士的一次合法移动是：沿一个方向移动两格，再沿与其垂直的方向移动一格。下图展示了骑士从一个格子出发时所有 8 种可能的移动方式。
# 示例 1：
# 输入： start = [1, 1], target = [2, 2]
# 输出： true
# 解释：
# 一种可行的移动序列为(1, 1) -> (3, 2) -> (2, 4) -> (4, 3) -> (2, 2)。
# 骑士经过 4 次移动到达目标位置，4 是偶数。因此答案为 true。
# 示例 2：
# 输入： start = [4, 5], target = [6, 6]
# 输出： false
# 解释：
# 骑士无法用偶数次移动从 start = [4, 5] 到达 target = [6, 6]。因此答案为 false。
# 提示：
# start.length == target.length == 2
# 0 <= start[i], target[i] <= 7

class Solution:
    def dfs(self, visited, x1, y1, x2, y2, step):
        if x1 < 0 or y1 < 0 or x1 >= 8 or y1 >= 8:
            return False
        if visited[x1][y1]:
            return False
        if x1 == x2 and y1 == y2:
            return step % 2 == 0
        visited[x1][y1] = True
        flag1 = self.dfs(visited, x1 + 2, y1 + 1, x2, y2, step + 1)
        flag2 = self.dfs(visited, x1 + 2, y1 - 1, x2, y2, step + 1)
        flag3 = self.dfs(visited, x1 - 2, y1 + 1, x2, y2, step + 1)
        flag4 = self.dfs(visited, x1 - 2, y1 - 1, x2, y2, step + 1)
        flag5 = self.dfs(visited, x1 + 1, y1 + 2, x2, y2, step + 1)
        flag6 = self.dfs(visited, x1 - 1, y1 + 2, x2, y2, step + 1)
        flag7 = self.dfs(visited, x1 + 1, y1 - 2, x2, y2, step + 1)
        flag8 = self.dfs(visited, x1 - 1, y1 - 2, x2, y2, step + 1)
        return flag1 or flag2 or flag3 or flag4 or flag5 or flag6 or flag7 or flag8
    
    def canReach1(self, start: list[int], target: list[int]) -> bool:
        visited = []
        for i in range(8):
            visited.append([False] * 8)
        step = 0
        return self.dfs(visited, start[0], start[1], target[0], target[1], step)
    
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2