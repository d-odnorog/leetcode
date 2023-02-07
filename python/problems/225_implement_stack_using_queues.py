# https://leetcode.com/problems/implement-stack-using-queues/


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.stack == []


if __name__ == '__main__':
    s = MyStack()

    assert not s.push(1)
    assert not s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()
