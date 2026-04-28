class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        tmp_queue = []
        tmp_queue.append(value)

        for val in self.queue:
            tmp_queue.append(val)

        self.queue = tmp_queue 

    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1 
        else:
            return self.queue.pop()

    def popleft(self) -> int:
        if len(self.queue) == 0:
            return -1 
        else:
            return self.queue.pop(0)
