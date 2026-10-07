# 2026.10.07力扣网刷题
# 4065. 移除不同值重排数组——中级工程师、数组、哈希表、计数、有序集合、排序、模拟、堆（优先队列）、第521场周赛——简单
# 给你一个整数数组 nums。
# 初始时，你有一个 空 数组 ans。重复执行以下操作，直到 nums 变为 空 ：
# 找出当前 nums 中 所有不同 的值。
# 将当前 nums 中每个 不同 的值各移除一个，并按 升序 将这些值依次添加到 ans 中。
# 返回数组 ans。
# 示例 1：
# 输入： nums = [3, 1, 3, 2, 1, 3]
# 输出：[1, 2, 3, 1, 3, 3]
# 解释：
# 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
# 1	1, 2, 3[3, 1, 3][1, 2, 3]
# 2	1, 3[3][1, 2, 3, 1, 3]
# 3	3[][1, 2, 3, 1, 3, 3]
# 此时 nums 已为空，因此答案为[1, 2, 3, 1, 3, 3]。
# 示例 2：
# 输入： nums = [7, 7, 4, 4, 4]
# 输出：[4, 7, 4, 7, 4]
# 解释：
# 操作	添加到 ans 的值	操作后的 nums	操作后的 ans
# 1	4, 7[7, 4, 4][4, 7]
# 2	4, 7[4][4, 7, 4, 7]
# 3	4[][4, 7, 4, 7, 4]
# 此时 nums 已为空，因此答案为[4, 7, 4, 7, 4]。
# 提示：
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        hash, dif = {}, 0
        for num in nums:
            if num not in hash:
                dif += 1
                hash[num] = 1
            else:
                hash[num] += 1
        keys = sorted(hash)
        ans = []
        while dif:
            for key in keys:
                if hash[key]:
                    ans.append(key)
                    hash[key] -= 1
                    if hash[key] == 0:
                        dif -= 1
        return ans