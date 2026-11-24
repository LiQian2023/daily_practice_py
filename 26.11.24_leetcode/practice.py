# 2026.11.24力扣网刷题
# 3411. 最长乘积等价子数组——中级工程师、数组、数学、枚举、数论、滑动窗口、第431场周赛——简单
# 给你一个由 正整数 组成的数组 nums。
# 如果一个数组 arr 满足 prod(arr) == lcm(arr) * gcd(arr)，则称其为 乘积等价数组 ，其中：
# prod(arr) 表示 arr 中所有元素的乘积。
# gcd(arr) 表示 arr 中所有元素的最大公因数(GCD)。
# lcm(arr) 表示 arr 中所有元素的最小公倍数(LCM)。
# 返回数组 nums 的 最长 乘积等价 子数组 的长度。
# 示例 1：
# 输入： nums = [1, 2, 1, 2, 1, 1, 1]
# 输出： 5
# 解释：
# 最长的乘积等价子数组是[1, 2, 1, 1, 1]，其中 prod([1, 2, 1, 1, 1]) = 2， gcd([1, 2, 1, 1, 1]) = 1，以及 lcm([1, 2, 1, 1, 1]) = 2。
# 示例 2：
# 输入： nums = [2, 3, 4, 5, 6]
# 输出： 3
# 解释：
# 最长的乘积等价子数组是[3, 4, 5]。
# 示例 3：
# 输入： nums = [1, 2, 3, 1, 4, 5, 1]
# 输出： 5
# 提示：
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 10

from typing import List


class Solution:
    def Get_Prime_List(self, x, primes):
        for i in range(2, int(x ** 0.5) + 1):
            while x % i == 0:
                if i not in primes:
                    primes.append(i)
                x //= i
            if 1 == x:
                break
        if x > 1:
            primes.append(x)
    
    def Check(self, primes):
        for prime in primes:
            if prime > 1:
                return True
        return False
    
    def Record(self, primes, gap, tmp):
        for i in tmp:
            primes[i] += gap
    
    def maxLength(self, nums: List[int]) -> int:
        primes, ans, n = [0] * 10, 2, len(nums)
        l, r = 0, 0
        while r < n:
            tmp = []
            self.Get_Prime_List(nums[r], tmp)
            self.Record(primes, 1, tmp)
            while self.Check(primes):
                tmp = []
                self.Get_Prime_List(nums[l], tmp)
                self.Record(primes, -1, tmp)
                l += 1
            if r - l + 1 > ans:
                ans = r - l + 1
            r += 1
        return ans