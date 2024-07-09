# 2024.07.09力扣网刷题
# 最小和分割——贪心、数学、排序——简单
# 给你一个正整数 num ，请你将它分割成两个非负整数 num1 和 num2 ，满足：
# num1 和 num2 直接连起来，得到 num 各数位的一个排列。
# 换句话说，num1 和 num2 中所有数字出现的次数之和等于 num 中所有数字出现的次数。
# num1 和 num2 可以包含前导 0 。
# 请你返回 num1 和 num2 可以得到的和的 最小 值。
# 注意：
# num 保证没有前导 0 。
# num1 和 num2 中数位顺序可以与 num 中数位顺序不同。
# 示例 1：
# 输入：num = 4325
# 输出：59
# 解释：我们可以将 4325 分割成 num1 = 24 和 num2 = 35 ，和为 59 ，59 是最小和。
# 示例 2：
# 输入：num = 687
# 输出：75
# 解释：我们可以将 687 分割成 num1 = 68 和 num2 = 7 ，和为最优值 75 。
# 提示：
# 10 <= num <= 10^9

def splitNum1(num):
    """
    :type num: int
    :rtype: int
    """
    num_list = []
    while num:
        num_list.append(num % 10)
        num //= 10
    num_list.sort()
    num1 = 0
    num2 = 0
    for i in range(0, len(num_list), 2):
        num1 *= 10
        num1 += num_list[i]
    for i in range(1, len(num_list), 2):
        num2 *= 10
        num2 += num_list[i]
    return num1 + num2


def splitNum(num):
    """
    :type num: int
    :rtype: int
    """
    num_list = ''.join(sorted(str(num)))
    return int(num_list[0::2]) + int(num_list[1::2])


a = int(input())
print(splitNum(a))
