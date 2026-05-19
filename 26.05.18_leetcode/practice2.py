# 2026.05.18力扣网刷题
# 89. a ^ b——位运算、快速幂——简单
# 求 a 的 b 次方对 p 取模的值。
# 输入格式
# 三个整数 a, b, p
# , 在同一行用空格隔开。
# 输出格式
# 输出一个整数，表示a^ b mod p的值。
# 数据范围
# 0≤a, b≤10^9
# 1≤p≤10^9
# 输入样例：
# 3 2 7
# 输出样例：
# 2
from urllib import parse


class Solution:
    def myPow(self, a: int, b: int, p: int)->int:
        ans = 1 % p
        while b:
            if b & 1:
                ans = ans * a % p
            a = a * a % p
            b >>= 1
        return ans
    
    def main(self):
        a, b, p = map(int, input().split())
        print(self.myPow(a, b, p))
    
if __name__ == '__main__':
    sol = Solution()
    sol.main()