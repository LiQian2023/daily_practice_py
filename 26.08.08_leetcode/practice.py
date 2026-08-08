# 2026.08.08力扣网刷题
# 4010. 数对的最大强度——中级工程师、第513场周赛——中等
# 给你一个整数数组 nums。
# 选择 恰好一对 不同下标 i 和 j。该数对的 强度 定义为：
# (nums[i] * nums[j]) / gcd(nums[i], nums[j])2
# 返回所有可能数对中的 最大 强度。
# gcd(a, b) 表示 a 和 b 的 最大公约数 。
# 示例 1：
# 输入： nums = [2, 3, 5]
# 输出： 15
# 解释：
# 选择 i = 1 和 j = 2，得到强度：
# (3 * 5) / gcd(3, 5)2 = 15 / 1 = 15，这是所有数对中的最大值。
# 示例 2：
# 输入： nums = [4, 6, 8]
# 输出： 12
# 解释：
# 选择 i = 1 和 j = 2，得到强度：
# (6 * 8) / gcd(6, 8)2 = 48 / 4 = 12，这是所有数对中的最大值。
# 示例 3：
# 输入： nums = [3, 3]
# 输出： 1
# 解释：
# 选择 i = 0 和 j = 1，得到强度：
# (3 * 3) / gcd(3, 3)2 = 9 / 9 = 1，这是唯一数对的强度。
# 提示：
# 2 <= nums.length <= 2000
# 1 <= nums[i] <= 10^5
from math import gcd
class Solution:
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while True:
            if a == 0 or b == 0:
                break
            tmp = a % b
            if tmp == 0:
                break
            a, b = b, tmp
        return b
    
    def maxPairStrength(self, nums: list[int]) -> int:
        ans, n = -1, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                g = gcd(nums[i], nums[j])
                tmp = nums[i] * nums[j] // (g * g)
                if tmp > ans:
                    ans = tmp
        return ans
    
    def maxPairStrength2(self, nums: list[int]) -> int:
        ans, n = -1, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                if b > a:
                    a, b = b, a
                while b:
                    a, b = b, a % b
                tmp = (nums[i] // a) * (nums[j] // a)
                if tmp > ans:
                    ans = tmp
        return ans