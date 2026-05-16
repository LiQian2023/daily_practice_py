# 2026.05.16力扣网刷题
# 面试题 03.04.化栈为队——栈、设计、队列——简单
# 实现一个MyQueue类，该类用两个栈来实现一个队列。
# 示例：
# MyQueue queue = new MyQueue();
# queue.push(1);
# queue.push(2);
# queue.peek();  // 返回 1
# queue.pop();   // 返回 1
# queue.empty(); // 返回 false
# 说明：
# 你只能使用标准的栈操作 -- 也就是只有 push to top, peek / pop from top, size 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushStack = []
        self.popStack = []
        self.pushTop = -1
        self.popTop = -1
        
    def transform(self, stack1, stack2, top1, top2):
        while top1 != -1:
            top1 -= 1
            stack2.append(stack1.pop())
            top2 += 1
        return top1, top2
    
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.pushTop, self.popTop = self.transform(self.popStack, self.pushStack, self.popTop, self.pushTop)
        self.pushTop += 1
        self.pushStack.append(x)
    
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.popTop, self.pushTop = self.transform(self.pushStack, self.popStack, self.pushTop, self.popTop)
        self.popTop -= 1
        return self.popStack.pop()
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.popTop, self.pushTop = self.transform(self.pushStack, self.popStack, self.pushTop, self.popTop)
        return self.popStack[self.popTop]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.popTop == -1 and self.pushTop == -1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()