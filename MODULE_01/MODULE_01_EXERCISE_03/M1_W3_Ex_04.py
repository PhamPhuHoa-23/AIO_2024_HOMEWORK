class MyQueue:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__queue = []
        self.__length__ = 0

    def is_empty(self):
        if self.__length__ == 0:
            return True
        return False

    def is_full(self):
        if self.__length__ == self.__capacity:
            return True
        return False

    def dequeue(self):
        if not self.is_empty():
            self.__length__ -= 1
            return self.__queue.pop(0)

    def enqueue(self, value):
        if not self.is_full():
            self.__length__ += 1
            self.__queue.append(value)

    def front(self):
        if not self.is_empty():
            return self.__queue[0]


# Unit test
if __name__ == '__main__':
    queue1 = MyQueue(capacity=5)

    queue1.enqueue(1)

    queue1.enqueue(2)

    print(queue1.is_full())  # FALSE

    print(queue1.front())  # 1

    print(queue1.dequeue())  # 1

    print(queue1.front())  # 2

    print(queue1.dequeue())  # 2

    print(queue1.is_empty())  # TRUE
