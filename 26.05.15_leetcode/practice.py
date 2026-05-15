# 2026.05.15力扣网刷题
# 面试题 03.02. 栈的最小值——栈、设计——简单
# 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。
# 示例：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.mt = -1
    
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.mt == -1 or x <= self.minStack[self.mt]:
            self.mt += 1
            self.minStack.append(x)
            
    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minStack[self.mt]:
            self.mt -= 1
            self.minStack.pop(-1)
        self.stack.pop(-1)
    
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()