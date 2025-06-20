# 2025.06.20力扣网刷题
# 最长乘积等价子数组——数组、数学、数论、枚举、滑动窗口——简单
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

class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_gcd_lcm(gcd, lcm, num):
            a = lcm
            while lcm % num or lcm % a or lcm % gcd:
                lcm += 1
                if a % gcd or num % gcd:
                    gcd -= 1
            while a % gcd or num % gcd:
                gcd -= 1
            return gcd, lcm
        def get_prob(nums, begin, end):
            prob = 1
            for i in range(begin, end + 1):
                prob *= nums[i]
            return prob
        gcd, lcm = nums[0], nums[0]
        i, j = 0, 1
        ans = 0
        length = len(nums)
        while i <= j < length:
            gcd, lcm = get_gcd_lcm(gcd, lcm, nums[j])
            prob1 = gcd * lcm
            prob2 = get_prob(nums, i, j)
            if prob1 == prob2:
                ans = max(ans, j - i + 1)
                j += 1
            else:
                i += 1
                gcd, lcm = nums[i], nums[i]
                j = i + 1
        return ans