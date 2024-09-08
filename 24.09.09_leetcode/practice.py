# 2024.09.09力扣网刷题
# 库存管理 III——数组、分治、快速选择、排序、堆（优先队列）——简单
# 仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。
# 请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。
# 示例 1：
# 输入：stock = [2, 5, 7, 4], cnt = 1
# 输出：[2]
# 示例 2：
# 输入：stock = [0, 2, 3, 6], cnt = 2
# 输出：[0, 2] 或[2, 0]
# 提示：
# 0 <= cnt <= stock.length <= 10000
# 0 <= stock[i] <= 10000

class Solution(object):
    def inventoryManagement(self, stock, cnt):
        """
        :type stock: List[int]
        :type cnt: int
        :rtype: List[int]
        """
        stock.sort()
        return stock[:cnt]