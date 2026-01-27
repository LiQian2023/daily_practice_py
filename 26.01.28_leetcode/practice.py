# 2026.01.28力扣网刷题
# LCR 179. 查找总价格为目标值的两个商品——数组、二分查找、双指针——简单
# 购物车内的商品价格按照升序记录于数组 price。请在购物车中找到两个商品的价格总和刚好是 target。若存在多种情况，返回任一结果即可。
# 示例 1：
# 输入：price = [3, 9, 12, 15], target = 18
# 输出：[3, 15] 或者[15, 3]
# 示例 2：
# 输入：price = [8, 21, 27, 34, 52, 66], target = 61
# 输出：[27, 34] 或者[34, 27]
# 提示：
# 1 <= price.length <= 10 ^ 5
# 1 <= price[i] <= 10 ^ 6
# 1 <= target <= 2 * 10 ^ 6

class Solution(object):
    def twoSum1(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [0, 0]
        hash = {}
        for p in price:
            if p not in hash:
                hash[p] = True
        for p in price:
            key = target - p
            if key in hash:
                ans[0] = p
                ans[1] = key
                break
        return ans

    def twoSum2(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        def BiSearch(price, length, l, r, key):
            while l <= r:
                m = (r - l) // 2 + l
                if key == price[m]:
                    return m
                elif key < price[m]:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        length = len(price)
        ans = [0, 0]
        for i in range(length):
            l, r = i + 1, length - 1
            key = target - price[i]
            if key < price[r]:
                ret = BiSearch(price, length, l, r, key)
                if ret != -1:
                    ans = [price[i], key]
                    break
            elif key == price[r]:
                ans = [price[i], key]
                break
        return ans

    def twoSum(self, price, target):
        """
        :type price: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [0, 0]
        l, r = 0, len(price) - 1
        while l < r:
            key = target - price[l]
            if key < price[r]:
                r -= 1
            elif key > price[r]:
                l += 1
            else:
                ans = [price[l], key]
                break
        return ans
