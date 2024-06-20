class MyStack:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__lst = []
        self.__length__ = 0

    def get_capacity(self): return self.__capacity

    def set_capacity(self, new_capacity: int): self.__capacity = new_capacity

    def is_empty(self):
        if self.__length__ == 0:
            return True
        return False

    def is_full(self):
        if self.__length__ == self.get_capacity():
            return True
        return False

    def pop(self):
        if not self.is_empty():
            self.__length__ -= 1
            return self.__lst.pop()

    def push(self, value):
        if not self.is_full():
            self.__lst.append(value)
            self.__length__ += 1

    def top(self): return self.__lst[-1]


# Unit test
if __name__ == '__main__':
    stack1 = MyStack(capacity=5)

    stack1.push(1)
    stack1.push(2)

    print(stack1.is_full())  # FALSE

    print(stack1.top())  # 2

    print(stack1.pop())  # 2

    print(stack1.top())  # 1

    print(stack1.pop())  # 1

    print(stack1.is_empty())  # TRUE
