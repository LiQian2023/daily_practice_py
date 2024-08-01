# 2024.08.01力扣网刷题
# 心算挑战——贪心、数组、排序——简单
# 「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，
# 若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。
# 给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。
# 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。
# 示例 1：
# 输入：cards = [1, 2, 8, 9], cnt = 3
# 输出：18
# 解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1 + 8 + 9 = 18。
# 示例 2：
# 输入：cards = [3, 3, 1], cnt = 1
# 输出：0
# 解释：不存在获取有效得分的卡牌方案。
# 提示：
# 1 <= cnt <= cards.length <= 10 ^ 5
# 1 <= cards[i] <= 1000


class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
        # 方法一：排序+模拟
        odd = []
        even = []
        # 分奇偶
        for card in cards:
            if card % 2 == 0:
                even.append(card)
            else:
                odd.append(card)
        # 奇偶降序
        odd.sort(reverse=True)
        even.sort(reverse=True)
        # 奇偶个数
        odd_len = len(odd)
        even_len = len(even)
        odd_pi, even_pi = 0, 0
        ans = 0
        # 处理cnt为奇数的情况
        if cnt % 2 and even_len:
            ans = even[0]
            even_pi = 1
            cnt -= 1
        elif cnt % 2 and even_len == 0:
            return 0
        # 获取奇数和与偶数和的最大值
        while odd_len - odd_pi >= 2 and even_len - even_pi >= 2 and cnt:
            even_sum = even[even_pi] + even[even_pi + 1]
            odd_sum = odd[odd_pi] + odd[odd_pi + 1]
            if odd_sum > even_sum:
                ans += odd_sum
                odd_pi += 2
                cnt -= 2
            else:
                ans += even_sum
                even_pi += 2
                cnt -= 2
        # 处理奇数个数不足cnt个时
        if odd_len - odd_pi < cnt:
            while even_len - even_pi >= cnt and cnt:
                ans += even[even_pi] + even[even_pi + 1]
                even_pi += 2
                cnt -= 2
        # 处理偶数个数不足cnt个时
        elif even_len - even_pi < cnt:
            while odd_len - odd_pi >= cnt and cnt:
                ans += odd[odd_pi] + odd[odd_pi + 1]
                odd_pi += 2
                cnt -= 2
        # 处理奇数与偶数个数兜不足cnt个时
        if cnt:
            ans = 0
        return ans


cards = [1, 3, 3, 6, 5, 3, 5, 3, 10, 6]
cnt = 9
print(Solution().maxmiumScore(cards, cnt))
