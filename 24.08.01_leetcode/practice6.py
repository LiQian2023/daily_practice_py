# 2024.08.01力扣网刷题
# 按照频率将数组升序排序——数组、哈希表、排序——简单
# 给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。
# 请你返回排序后的数组。
# 示例 1：
# 输入：nums = [1, 1, 2, 2, 2, 3]
# 输出：[3, 1, 1, 2, 2, 2]
# 解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
# 示例 2：
# 输入：nums = [2, 3, 1, 3, 2]
# 输出：[1, 3, 3, 2, 2]
# 解释：'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。
# 示例 3：
# 输入：nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
# 输出：[5, -1, 4, 4, -6, -6, 1, 1, 1]
# 提示：
# 1 <= nums.length <= 100
# - 100 <= nums[i] <= 100

class Solution(object):
    def frequencySort1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Python3：哈希表
        tmp = list(set(nums))
        tmp.sort(reverse=True)
        nums_dict = {}
        for i in tmp:
            nums_dict[i] = nums.count(i)
        tmp = sorted(nums_dict, key=lambda x: nums_dict[x])
        ans = []
        for i in tmp:
            ans += [i] * nums_dict[i]
        print(ans)
        return ans

    def frequencySort2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Python2：哈希表
        # 去重
        tmp_list = list(set(nums))
        # 以频率为关键字创建字典
        count_dict = {}
        for i in tmp_list:
            if nums.count(i) not in count_dict:
                count_dict[nums.count(i)] = [i]
            else:
                count_dict[nums.count(i)].append(i)
            if len(count_dict[nums.count(i)]) > 1:
                count_dict[nums.count(i)].sort(reverse=True)  # 值降序
        # 关键字列表——升序
        key_list = sorted(count_dict)
        ans = []
        # 按照关键字获取值
        for i in key_list:
            for j in count_dict[i]:
                ans += [j] * i
        return ans

    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Python2：哈希表优化
        tmp_list = list(set(nums))
        count_list = []
        for i in tmp_list:
            count_list.append([i, nums.count(i)])
        count_list.sort(key=lambda x: x[1], reverse=True)
        nums_dict = {}
        for i in range(len(count_list)):
            if count_list[i][1] not in nums_dict:
                nums_dict[count_list[i][1]] = [count_list[i][0]]
            else:
                nums_dict[count_list[i][1]].append(count_list[i][0])
        print(nums_dict)
        for i in nums_dict:
            nums_dict[i].sort(reverse=True)
        nums_dict_list = sorted(nums_dict)
        print(nums_dict_list)
        ans = []
        for i in nums_dict_list:
            for j in nums_dict[i]:
                ans += [j] * i
        return ans
nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
Solution().frequencySort(nums)
