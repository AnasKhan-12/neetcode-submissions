class MyStack:

    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # what we did to pop we will do it to push
        # for each member pushed we will remove the previous members and move them ahead of the current member
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())


    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0] # as the queue is now reversed so top (last added element) would be q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()