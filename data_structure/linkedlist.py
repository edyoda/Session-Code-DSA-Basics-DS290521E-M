class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # Storing the number of nodes in LL

    def create_ll(self, node_value):
        self.head = None
        self.tail = None
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node

    def exists(self):
        return self.head is not None

    def insert(self, node_value, location):
        if not self.exists():
            print("[ERROR] : LL Does Not Exists")
            return
        new_node = Node(node_value)
        if location == 0:
            new_node.next = self.head
            self.head = new_node
        elif location >= self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for i in range(0, location-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.size = self.size + 1

    def traversal(self):
        curr_node = self.head
        while curr_node is not None:
            print("{}".format(curr_node.data), end=" -> ")
            curr_node = curr_node.next


if __name__ == '__main__':
    single_ll = SingleLL()
    single_ll.create_ll(10)
    single_ll.insert(20, 0)
    single_ll.insert(30, 0)
    single_ll.insert(40, 10)
    single_ll.traversal()