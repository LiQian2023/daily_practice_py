# 2024.09.10力扣网刷题
# 库存管理 II——数组、哈希表、分治、计数、排序——简单
# 仓库管理员以数组 stock 形式记录商品库存表。stock[i] 表示商品 id，可能存在重复。请返回库存表中数量大于 stock.length / 2 的商品 id。
# 示例 1:
# 输入: stock = [6, 1, 3, 1, 1, 1]
# 输出 : 1
# 限制：
# 1 <= stock.length <= 50000
# 给定数组为非空数组，且存在结果数字

class Solution(object):
    def inventoryManagement(self, stock):
        """
        :type stock: List[int]
        :rtype: int
        """
        # 方法一：sort排序
        stock.sort()
        l, r = 0, 0
        length = len(stock)
        key = length // 2
        while r < length:
            if stock[l] == stock[r]:
                r += 1
            else:
                if r - l > key:
                    break
                else:
                    l = r
        return stock[l]
