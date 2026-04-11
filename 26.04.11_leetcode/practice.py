# 2026.04.11力扣网刷题
# LCR 147. 最小栈——栈、设计——简单
# 请你设计一个 最小栈 。它提供 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 实现 MinStack 类 :
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
# 示例 1：
# 输入：
# ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
# [[], [-2], [0], [-3], [], [], [], []]
# 输出：
# [null, null, null, null, -3, null, 0, -2]
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 - 3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 - 2.
# 提示：
# - 2^31 <= val <= 2^31 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push、pop、top 和 getMin 最多被调用 3 * 10^4 次
# 注意：本题与主站 155 题相同：https://leetcode.cn/problems/min-stack/

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.Min = None
        self.Top = -1
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.Top += 1
        if self.Min == None or x < self.Min:
            self.Min = x
    
    def pop(self):
        """
        :rtype: None
        """
        num = self.top()
        self.stack.pop()
        self.Top -= 1
        if self.Top == -1:
            self.Min = None
        elif self.Min == num:
            self.Min = min(self.stack)
            
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.Top]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.Min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()