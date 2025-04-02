class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class s_linked_list:
    def __init__(self):
        self.head = None
        return
    
    def add_end(self, data):

        if data is None:
            return

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node
    
    def add_nodes_list(self, values):
        
        if values:
            for value in values:
                self.add_end(value)

    def traverse_f(self, node=None, nodes=None):
        if nodes is None:
            nodes = []

        if node:
            nodes.append(node.data)
            self.traverse_f(node.next, nodes)

        return nodes

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def get_mid_list(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

nodes = [7, 12, 15]
linked_list = s_linked_list()

linked_list.add_nodes_list(nodes)
l = linked_list.traverse_f(linked_list.head)
print(f"{l}")

linked_list.reverse()

print("After reverse:", linked_list.traverse_f(linked_list.head))