# 2026.05.24力扣网刷题
# 92. 递归实现指数型枚举——递归——简单
# 从 1∼n 这 n 个整数中随机选取任意多个，输出所有可能的选择方案。
# 输入格式
# 输入一个整数 n。
# 输出格式
# 每行输出一种方案。
# 同一行内的数必须升序排列，相邻两个数用恰好 1
# 个空格隔开。
# 对于没有选任何数的方案，输出空行。
# 本题有自定义校验器（SPJ），各行（不同方案）之间的顺序任意。
# 数据范围
# 1≤n≤15
# 输入样例：
# 3
# 输出样例：
# 3
# 2
# 2 3
# 1
# 1 3
# 1 2
# 1 2 3

class Solution:
    def dfs(self, n, path, pi):
        if n == 0:
            if pi == 0:
                print('\n')
            else:
                outPut = ' '.join(map(str, reversed(path)))
                print(outPut)
            return
        path.append(n)
        pi += 1
        self.dfs(n - 1, path, pi)
        path.pop()
        pi -= 1
        self.dfs(n - 1, path, pi)
    
    def main(self):
        n = int(input())
        path = list()
        self.dfs(n, path, 0)
    
if __name__ == '__main__':
    sol = Solution()
    sol.main()