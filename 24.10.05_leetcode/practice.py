# 2024.10.05力扣网刷题
# 前 K 个高频元素——数组、哈希表、分治、桶排序、计数、快速选择、排序、堆（优先队列）——中等
# 给你一个整数数组nums和一个整数k ，请你返回其中出现频率前k高的元素。你可以按任意顺序返回答案。
# 示例1:
# 输入: nums = [1, 1, 1, 2, 2, 3], k = 2
# 输出: [1, 2]
# 示例2:
# 输入: nums = [1], k = 1
# 输出: [1]
# 提示：
# 1 <= nums.length <= 10^5
# k的取值范围是[1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前k个高频元素的集合是唯一的
# 进阶：你所设计算法的时间复杂度必须优于O(nlogn) ，其中n是数组大小。


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_list = sorted(set(nums))
        nums_dict = dict(zip(nums_list, [nums.count(i) for i in nums_list]))
        ans = sorted(nums_dict.keys(), key=lambda x: nums_dict[x], reverse=True)
        return ans[:k]


nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
