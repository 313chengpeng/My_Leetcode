# 设计一个支持
# push ，pop ，top
# 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现
# MinStack
# 类:
#
# MinStack()
# 初始化堆栈对象。
# void
# push(int
# val) 将元素val推入堆栈。
# void
# pop()
# 删除堆栈顶部的元素。
# int
# top()
# 获取堆栈顶部的元素。
# int
# getMin()
# 获取堆栈中的最小元素。
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)
    print(a.getMin())
    a.pop()
    print(a.top())
    print(a.getMin())