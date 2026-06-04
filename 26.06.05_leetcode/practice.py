# 2026.06.05力扣网刷题
# 面试题 03.01.三合一 —— 栈、设计、数组——简单
# 三合一。描述如何只用一个数组来实现三个栈。
# 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
# 构造函数会传入一个stackSize参数，代表每个栈的大小。
# 示例 1：
# 输入：
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
# 输出：
# [null, null, null, 1, -1, -1, true]
# 说明：当栈为空时`pop, peek`返回 - 1，当栈满时`push`不压入元素。
# 示例 2：
# 输入：
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
# [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
# 输出：
# [null, null, null, null, 2, 1, -1, -1]
# 提示：
# 0 <= stackNum <= 2

class TripleInOne:
    
    def __init__(self, stackSize: int):
        self.stack = [-1] * stackSize * 3
        self.index = [0, stackSize, stackSize * 2]
        self.top = [0, stackSize, stackSize * 2]
        self.size = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self.top[stackNum] == self.index[stackNum] + self.size:
            return
        self.stack[self.top[stackNum]] = value
        self.top[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.top[stackNum] == self.index[stackNum]:
            return -1
        ans = self.stack[self.top[stackNum] - 1]
        self.top[stackNum] -= 1
        return ans

    def peek(self, stackNum: int) -> int:
        if self.top[stackNum] == self.index[stackNum]:
            return -1
        return self.stack[self.top[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.top[stackNum] == self.index[stackNum]

# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)