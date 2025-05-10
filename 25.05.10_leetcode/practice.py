# 2025.05.10力扣网刷题
# 计算子数组的 x - sum I——数组、哈希表、滑动窗口、堆——简单
# 给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
# 数组的 x - sum 计算按照以下步骤进行：
# 统计数组中所有元素的出现次数。
# 仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
# 计算结果数组的和。
# 注意，如果数组中的不同元素少于 x 个，则其 x - sum 是数组的元素总和。
# 返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x - sum。
# 子数组 是数组内的一个连续 非空 的元素序列。
# 示例 1：
# 输入：nums = [1, 1, 2, 2, 3, 4, 2, 3], k = 6, x = 2
# 输出：[6, 10, 12]
# 解释：
# 对于子数组[1, 1, 2, 2, 3, 4]，只保留元素 1 和 2。因此，answer[0] = 1 + 1 + 2 + 2。
# 对于子数组[1, 2, 2, 3, 4, 2]，只保留元素 2 和 4。因此，answer[1] = 2 + 2 + 2 + 4。注意 4 被保留是因为其数值大于出现其他出现次数相同的元素（3 和 1）。
# 对于子数组[2, 2, 3, 4, 2, 3]，只保留元素 2 和 3。因此，answer[2] = 2 + 2 + 2 + 3 + 3。
# 示例 2：
# 输入：nums = [3, 8, 7, 8, 7, 5], k = 2, x = 2
# 输出：[11, 15, 15, 15, 12]
# 解释：
# 由于 k == x，answer[i] 等于子数组 nums[i..i + k - 1] 的总和。
# 提示：
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50
# 1 <= x <= k <= nums.length

from collections import OrderedDict

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        my_dict = {}
        length = len(nums)
        left, right = 0, 0
        ans = []
        while right <= length:
            while right < left + k:
                key_hash = nums[right]
                if key_hash in my_dict:
                    my_dict[key_hash] += 1
                else:
                    my_dict[key_hash] = 1
                right += 1
            my_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: (-x[1], -x[0])))
            tmp, n1, n2 = 0, 0, 0
            for key in my_dict:
                tmp += key * my_dict[key]
                n1 += 1
                n2 += my_dict[key]
                if n1 == x or n2 >= k:
                    break
            ans.append(tmp)
            my_dict[nums[left]] -= 1
            if my_dict[nums[left]] == 0:
                del my_dict[nums[left]]
            left += 1
            if right == length:
                break
            if nums[right] not in my_dict:
                my_dict[nums[right]] = 1
            else:
                my_dict[nums[right]] += 1
            right += 1
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3, 4, 2, 3]
    k = 6
    x = 2
    print(Solution().findXSum(nums, k, x))
