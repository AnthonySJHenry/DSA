class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def reverse_string(my_string):
    reversed_string = ""

    # Create a stack
    stack = Stack()

    # Iterate through my_string and push the chars onto the stack.
    for char in my_string:
        stack.push(char)

    # Pop the chars off the stack and append to reversed_string
    while not stack.is_empty():
        reversed_string += stack.pop()

    # Return reversed_string
    return reversed_string
