class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # CreateQueue() function
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, node_value):
        new_node = Node(node_value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head is None

    def dequeue(self):
        if self.is_empty():
            print("[ERROR] : Queue is Empty")
            return
        temp_node = self.head
        self.head = self.head.next
        return temp_node.data

    def peek(self):
        if self.is_empty():
            print("[ERROR] : Queue is Empty")
            return
        return self.head.data

    def delete(self):
        self.head = None
        self.tail = None

    def display(self):
        current_node = self.head
        while current_node is not None:
            print("{}".format(current_node.data), end=" -> ")
            current_node = current_node.next
        print("")


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10) # 1
    queue.enqueue(20) # 2
    queue.enqueue(30) # 3
    queue.display()
    print("Dequeue {}".format(queue.dequeue()))
    queue.display()








