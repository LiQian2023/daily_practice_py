# 2026.09.18力扣网刷题
# 79. 单词搜索——深度优先搜索、数组、字符串、回溯、矩阵——中等
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 示例 1：
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "ABCCED"
# 输出：true
# 示例 2：
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "SEE"
# 输出：true
# 示例 3：
# 输入：board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], word = "ABCB"
# 输出：false
# 提示：
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？

class Solution:
    def dfs(self, board, word, visited, move, x, y, z):
        if z == len(word):
            return True
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[x]):
            return False
        if visited[x][y]:
            return False
        if board[x][y] != word[z]:
            return False
        visited[x][y] = True
        res = False
        i, j = 0, 1
        while not res and j < 8:
            res = self.dfs(board, word, visited, move, x + move[i], y + move[j], z + 1)
            i += 2
            j += 2
        visited[x][y] = False
        return res
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        move = [0, 1, 0, -1, 1, 0, -1, 0]
        visited = []
        row, col = len(board), len(board[0])
        for i in range(row):
            visited.append([False] * col)
        ans = False
        i = 0
        while not ans and i < row:
            j = 0
            while not ans and j < col:
                if board[i][j] == word[0]:
                    ans = self.dfs(board, word, visited, move, i, j, 0)
                j += 1
            i += 1
        return ans
        