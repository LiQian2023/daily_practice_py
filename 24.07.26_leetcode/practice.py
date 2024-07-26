# 2024.07.26力扣网刷题
# 公平的糖果交换——数组、哈希表、二分查找、排序——简单
# 爱丽丝和鲍勃拥有不同总数量的糖果。给你两个数组 aliceSizes 和 bobSizes ，
# aliceSizes[i] 是爱丽丝拥有的第 i 盒糖果中的糖果数量，bobSizes[j] 是鲍勃拥有的第 j 盒糖果中的糖果数量。
# 两人想要互相交换一盒糖果，这样在交换之后，他们就可以拥有相同总数量的糖果。一个人拥有的糖果总数量是他们每盒糖果数量的总和。
# 返回一个整数数组 answer，其中 answer[0] 是爱丽丝必须交换的糖果盒中的糖果的数目，answer[1] 是鲍勃必须交换的糖果盒中的糖果的数目。
# 如果存在多个答案，你可以返回其中 任何一个 。题目测试用例保证存在与输入对应的答案。
# 示例 1：
# 输入：aliceSizes = [1, 1], bobSizes = [2, 2]
# 输出：[1, 2]
# 示例 2：
# 输入：aliceSizes = [1, 2], bobSizes = [2, 3]
# 输出：[1, 2]
# 示例 3：
# 输入：aliceSizes = [2], bobSizes = [1, 3]
# 输出：[2, 3]
# 示例 4：
# 输入：aliceSizes = [1, 2, 5], bobSizes = [2, 4]
# 输出：[5, 4]
# 提示：
# 1 <= aliceSizes.length, bobSizes.length <= 10^4
# 1 <= aliceSizes[i], bobSizes[j] <= 10^5
# 爱丽丝和鲍勃的糖果总数量不同。
# 题目数据保证对于给定的输入至少存在一个有效答案。

class Solution(object):
    def fairCandySwap1(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        # 排序
        aliceSizes.sort()
        bobSizes.sort()
        # 查找
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        x = abs(sum1 - sum2) / 2
        ans = [0, 0]
        count1 = 0
        count2 = 0
        if sum1 < sum2:
            while not count1 or not count2:
                ans[0] += 1
                ans[1] = ans[0] + x
                count1 = aliceSizes.count(ans[0])
                count2 = bobSizes.count(ans[1])
        else:
            while not count1 or not count2:
                ans[1] += 1
                ans[0] = ans[1] + x
                count1 = aliceSizes.count(ans[0])
                count2 = bobSizes.count(ans[1])
        return ans

    def fairCandySwap2(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        x = abs(sum1 - sum2) / 2
        ans = [0, 0]
        count1 = 0
        count2 = 0
        if sum1 < sum2:
            while not count1 or not count2:
                ans[0] += 1
                ans[1] = ans[0] + x
                count1 = aliceSizes.count(ans[0])
                count2 = bobSizes.count(ans[1])
        else:
            while not count1 or not count2:
                ans[1] += 1
                ans[0] = ans[1] + x
                count1 = aliceSizes.count(ans[0])
                count2 = bobSizes.count(ans[1])
        return ans

    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        x = abs(sum1 - sum2) / 2
        ans = [0, 0]
        flag1 = False
        flag2 = False
        if sum1 < sum2:
            while not flag1 or not flag2:
                ans[0] += 1
                ans[1] = ans[0] + x
                flag1 = ans[0] in aliceSizes
                flag2 = ans[1] in bobSizes
        else:
            while not flag1 or not flag2:
                ans[1] += 1
                ans[0] = ans[1] + x
                flag1 = ans[0] in aliceSizes
                flag2 = ans[1] in bobSizes
        return ans
