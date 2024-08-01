# 2024.08.01力扣网刷题
# 元素计数——数组、排序——简单
# 给你一个整数数组 nums ，统计并返回在 nums 中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。
# 示例 1：
# 输入：nums = [11, 7, 2, 15]
# 输出：2
# 解释：元素 7 ：严格较小元素是元素 2 ，严格较大元素是元素 11 。
# 元素 11 ：严格较小元素是元素 7 ，严格较大元素是元素 15 。
# 总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。
# 示例 2：
# 输入：nums = [-3, 3, 3, 90]
# 输出：2
# 解释：元素 3 ：严格较小元素是元素 - 3 ，严格较大元素是元素 90 。
# 由于有两个元素的值为 3 ，总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。
# 提示：
# 1 <= nums.length <= 100
# - 10^5 <= nums[i] <= 10^5

class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort排序
        nums.sort()
        max_num = max(nums)
        min_num = min(nums)
        ans = len(nums) - nums.count(max_num) - nums.count(min_num)
        if ans < 0:
            ans = 0
        return ans