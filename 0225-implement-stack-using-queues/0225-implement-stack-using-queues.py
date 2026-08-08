from collections import deque

class MyStack:
    def __init__(self):
        self.queue_main = deque()
        self.queue_temp = deque()

    def push(self, x: int) -> None:
        self.queue_temp.append(x)

        while self.queue_main:
            self.queue_temp.append(self.queue_main.popleft())

        self.queue_main, self.queue_temp = self.queue_temp, self.queue_main

    def pop(self) -> int:
        return self.queue_main.popleft()

    def top(self) -> int:
        return self.queue_main[0]

    def empty(self) -> bool:
        return len(self.queue_main) == 0