# 2025.06.06力扣网刷题
# 寻找图中是否存在路径——深度优先搜索、广度优先搜索、并查集、图——简单
# 有一个具有 n 个顶点的 双向 图，其中每个顶点标记从 0 到 n - 1（包含 0 和 n - 1）。
# 图中的边用一个二维整数数组 edges 表示，其中 edges[i] = [ui, vi] 表示顶点 ui 和顶点 vi 之间的双向边。 
# 每个顶点对由 最多一条 边连接，并且没有顶点存在与自身相连的边。
# 请你确定是否存在从顶点 source 开始，到顶点 destination 结束的 有效路径 。
# 给你数组 edges 和整数 n、source 和 destination，如果从 source 到 destination 存在 有效路径 ，则返回 true，否则返回 false 。
# 示例 1：
# 输入：n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2
# 输出：true
# 解释：存在由顶点 0 到顶点 2 的路径:
# -0 → 1 → 2
# - 0 → 2
# 示例 2：
# 输入：n = 6, edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source = 0, destination = 5
# 输出：false
# 解释：不存在由顶点 0 到顶点 5 的路径.
# 提示：
# 1 <= n <= 2 * 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# 不存在重复边
# 不存在指向顶点自身的边

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        parent = [0] * n
        rank = [0] * n
        # 初始化父结点，每个结点单独成一个集合
        for i in range(n):
            parent[i] = i
        # 查找父结点
        def Find(parent, x):
            if parent[x] != x:
                parent[x] = Find(parent, parent[x])
            return parent[x]
        # 按秩合并
        def Union(parent, rank, x, y):
            root_x = Find(parent, x)
            root_y = Find(parent, y)
            if root_x != root_y:
                # 秩小的集合合并到秩大的集合
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y
                    rank[root_y] += 1
            return parent, rank
        len_edge = len(edges)
        for i in range(len_edge):
            x, y = edges[i][0], edges[i][1]
            parent, rank = Union(parent, rank, x, y)
        return Find(parent, source) == Find(parent, destination)