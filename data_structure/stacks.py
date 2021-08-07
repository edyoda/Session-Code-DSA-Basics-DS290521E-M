class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, node_value):
        new_node = Node(node_value)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top is None

    def pop(self):
        if self.is_empty():
            print("[ERROR] : Stack is empty")
            return
        temp_node = self.top
        self.top = self.top.next
        return temp_node.data

    def peek(self):
        if self.is_empty():
            print("[ERROR] : Stack is empty")
            return
        return self.top.data

    def display_values(self):
        current_node = self.top
        while current_node is not None:
            print("{}".format(current_node.data), end = " -> ")
            current_node = current_node.next
        print("")


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display_values()
    print("Popped {} ".format(stack.pop()))
    stack.display_values()








