class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        else:
            return False

    def add_node(self, node):
        if self.empty():
            self.head = node

        else:
            node.next = self.head
            self.head = node

    def search(self, target):
        cur = self.head
        while cur:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def delete(self, target):
        if self.head.data == target:
            self.head = self.head.next
            return

        cur = self.head

        while cur.next:
            if cur.next.data == target:
                cur.next = cur.next.next
                return
            cur = cur.next

        return None

        # cur = self.head.next
        # prev = self.head
        #
        # while cur:
        #     if cur.data == target:
        #         prev.next = cur.next
        #         return
        #     cur = cur.next
        #     prev = prev.next
        #
        # return None


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    s_li = SingleLinkedList()
    s_li.add_node(node1)
    s_li.add_node(node2)
    s_li.add_node(node3)
    s_li.add_node(node4)
    s_li.add_node(node5)

    print(s_li.search(5).data)
    print(s_li.search(6))

    s_li.delete(1)
    s_li.delete(2)
    s_li.delete(3)
    s_li.delete(4)
    s_li.delete(5)

    print(s_li.empty())

    print(s_li.search(1))
    print(s_li.search(5))
