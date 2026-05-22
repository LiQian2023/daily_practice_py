# 2026.05.21力扣网刷题
# 5579. 增加模数——快速幂——简单
# 给定 H 对非负整数数对 (Ai,Bi) 和一个正整数 M。
# 请你计算并输出 (AB11+AB22+…+ABHH) mod M。
# 输入格式
# 第一行包含整数 T，表示共有 T组测试数据。
# 每组数据第一行包含整数 M。
# 第二行包含整数 H。
# 接下来 H 行，每行包含两个整数 Ai,Bi。
# 输出格式
# 每组数据输出一行结果。
# 数据范围
# 1≤T≤100,
# 1≤M≤45000,
# 1≤H≤45000,
# 0≤Ai,Bi≤10^7,
# Ai和 Bi不同时为 0。
# 输入样例：
# 3
# 16
# 4
# 2 3
# 3 4
# 4 5
# 5 6
# 36123
# 1
# 2374859 3029382
# 17
# 1
# 3 18132
# 输出样例：
# 2
# 13195
# 13
import sys
class Solution:
    def myPow(self, a: int, b: int, m: int) -> int:
        res = 1 % m
        while b:
            if b & 1:
                res = res * a % m
            a = a * a % m
            b >>= 1
        return res
    
    def main(self):
        data = sys.stdin.read().split()
        t = int(data[0])
        index = 1
        for i in range(t):
            m, n = int(data[index]), int(data[index+1])
            index += 2
            ans = 0
            for j in range(n):
                a, b = int(data[index]), int(data[index+1])
                index += 2
                ans = (ans + self.myPow(a, b, m)) % m
            print(ans)
    
if __name__ == '__main__':
    sol = Solution()
    sol.main()
    
    