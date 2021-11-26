class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            return "Empty list, nothing to pop."
        return self.items.pop()

    def get_stack_items(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(123)
    stack1.push(456)
    print(stack1.get_stack_items())
    stack1.pop()
    print(stack1.peek())
    print(stack1.is_empty())
