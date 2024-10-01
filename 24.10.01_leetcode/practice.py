# 2024.10.01力扣网刷题
# 最大数——贪心、数组、字符串、排序——中等
# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 示例 1：
# 输入：nums = [10, 2]
# 输出："210"
# 示例 2：
# 输入：nums = [3, 30, 34, 5, 9]
# 输出："9534330"
# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9


class Solution(object):
    def MergeSort(self, a, left, right, b):
        if left >= right:
            return
        key = (right - left) // 2
        Solution().MergeSort(a, left, left + key, b)
        Solution().MergeSort(a, left + key + 1, right, b)
        size = left
        i, j = left, left + key + 1
        while i <= left + key and j <= right:
            tmp1 = a[i] + a[j]
            tmp2 = a[j] + a[i]
            if tmp1 > tmp2:
                b[size] = a[i]
                i += 1
            else:
                b[size] = a[j]
                j += 1
            size += 1
        while i <= left + key:
            b[size] = a[i]
            i += 1
            size += 1
        while j <= right:
            b[size] = a[j]
            j += 1
            size += 1
        for i in range(left, right + 1):
            a[i] = b[i]

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        length = len(nums)
        # 数字转字符串
        for i in range(length):
            nums[i] = str(nums[i])
        tmp = [0] * length
        Solution().MergeSort(nums, 0, len(nums) - 1, tmp)
        ans = ''.join(nums)
        if ans[0] == '0':
            ans = '0'
        return ans


nums =[1,2,3,4,5,6,7,8,9,0]
print(Solution().largestNumber(nums))