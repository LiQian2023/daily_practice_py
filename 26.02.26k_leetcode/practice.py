# 2026.02.26力扣网刷题
# 232. 用栈实现队列——栈、设计、队列——简单
# 请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：
# 实现 MyQueue 类：
# void push(int x) 将元素 x 推到队列的末尾
# int pop() 从队列的开头移除并返回元素
# int peek() 返回队列开头的元素
# boolean empty() 如果队列为空，返回 true ；否则，返回 false
# 说明：
# 你 只能 使用标准的栈操作 —— 也就是只有 push to top, peek / pop from top, size, 和 is empty 操作是合法的。
# 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
# 示例 1：
# 输入：
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 输出：
# [null, null, null, 1, 1, false]
# 解释：
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
# 提示：
# 1 <= x <= 9
# 最多调用 100 次 push、pop、peek 和 empty
# 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
# 进阶：
# 你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

class Stack(object):
    def __init__(self):
        self.data = []
        self.size = 0
        self.top = -1

    def isEmpty(self):
        return self.size == 0

    def S_push(self, x):
        self.top += 1
        self.data.append(x)
        self.size += 1

    def S_pop(self):
        x = self.data.pop(self.top)
        self.top -= 1
        self.size -= 1
        return x

    def S_peek(self):
        return self.data[self.top]


class MyQueue(object):
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()
        self.len = 0

    def push_to_pop(self):
        popTop = self.pushStack.top
        for i in range(popTop, -1, -1):
            enum = self.pushStack.S_pop()
            self.popStack.S_push(enum)

    def pop_to_push(self):
        pushTop = self.popStack.top
        for i in range(pushTop, -1, -1):
            enum = self.popStack.S_pop()
            self.pushStack.S_push(enum)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.pop_to_push()
        self.pushStack.S_push(x)
        self.len += 1

    def pop(self):
        """
        :rtype: int
        """
        self.push_to_pop()
        x = self.popStack.S_pop()
        self.len -= 1
        return x

    def peek(self):
        """
        :rtype: int
        """
        self.push_to_pop()
        return self.popStack.S_peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.len == 0