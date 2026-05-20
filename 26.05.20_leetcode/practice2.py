# 2026.05.20力扣网刷题
# 90. 64位整数乘法——位运算——简单
# 求 a 乘 b 对 p 取模的值。
# 输入格式
# 第一行输入整数a，第二行输入整数b，第三行输入整数p。
# 输出格式
# 输出一个整数，表示a * b mod p的值。
# 数据范围
# 1≤a, b, p≤10^18
# 输入样例：
# 3
# 4
# 5
# 输出样例：
# 2

import sys

class Solution:
    def myMul(self, a: int, b: int, p: int)->int:
        ans = 0
        while b > 0:
            if b & 1:
                ans = (ans + a) % p
            a = a * 2 % p
            b >>= 1
        return ans
    
    def main(self):
        data = sys.stdin.read().split()
        a, b, p = int(data[0]), int(data[1]), int(data[2])
        ans = self.myMul(a, b, p)
        print(ans)
    
if __name__ == '__main__':
    ans = Solution()
    ans.main()