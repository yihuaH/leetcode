#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.inn = [] # the stack when we want to push queue
        self.out = [] # the stack when we want to pop
    def push(self, x: int) -> None:
        self.inn.append(x)

    def pop(self) -> int:
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop()) 
        return self.out.pop()

    def peek(self) -> int:
        if len(self.out) == 0:
            while len(self.inn):
                self.out.append(self.inn.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return not (self.inn or self.out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

