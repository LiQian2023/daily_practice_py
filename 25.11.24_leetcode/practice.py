# 25.11.24力扣网刷题
# 2558. 从数量最多的堆取走礼物——数组、模拟、堆（优先队列）、第 331 场周赛——简单
# 给你一个整数数组 gifts ，表示各堆礼物的数量。每一秒，你需要执行以下操作：
# 选择礼物数量最多的那一堆。
# 如果不止一堆都符合礼物数量最多，从中选择任一堆即可。
# 将堆中的礼物数量减少到堆中原来礼物数量的平方根，向下取整。
# 返回在 k 秒后剩下的礼物数量。
# 示例 1：
# 输入：gifts = [25, 64, 9, 4, 100], k = 4
# 输出：29
# 解释：
# 按下述方式取走礼物：
# - 在第一秒，选中最后一堆，剩下 10 个礼物。
# - 接着第二秒选中第二堆礼物，剩下 8 个礼物。
# - 然后选中第一堆礼物，剩下 5 个礼物。
# - 最后，再次选中最后一堆礼物，剩下 3 个礼物。
# 最后剩下的礼物数量分别是[5, 8, 9, 4, 3] ，所以，剩下礼物的总数量是 29 。
# 示例 2：
# 输入：gifts = [1, 1, 1, 1], k = 4
# 输出：4
# 解释：
# 在本例中，不管选中哪一堆礼物，都必须剩下 1 个礼物。
# 也就是说，你无法获取任一堆中的礼物。
# 所以，剩下礼物的总数量是 4 。
# 提示：
# 1 <= gifts.length <= 10^3
# 1 <= gifts[i] <= 10^9
# 1 <= k <= 10^3

class Solution(object):
    def pickGifts1(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        def Creat_Heap(gifts, length):
            for i in range((length - 1) // 2, -1, -1):
                Adjust_down(gifts, length, i)

        def Adjust_down(gifts, length, parent):
            child = parent * 2 + 1
            while child < length:
                if child + 1 < length and gifts[child] > gifts[child + 1]:
                    child = child + 1
                if gifts[child] < gifts[parent]:
                    gifts[child], gifts[parent] = gifts[parent], gifts[child]
                parent = child
                child = parent * 2 + 1

        def Heap_sort(gifts, length):
            for i in range(length - 1 , 0, -1):
                gifts[i], gifts[0] = gifts[0], gifts[i]
                Adjust_down(gifts, i, 0)

        length = len(gifts)
        Creat_Heap(gifts, length)
        Heap_sort(gifts, length)

        for i in range(k):
            gifts[0] = int(gifts[0] ** 0.5)
            Creat_Heap(gifts, length)
            Heap_sort(gifts, length)

        return sum(gifts)

    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0] = int(gifts[0] ** 0.5)
        return sum(gifts)