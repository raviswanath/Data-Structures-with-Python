# Implementation of a double linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList():
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def add_before_node(self, key, data):
        curr = self.head
        while curr:
            if curr is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                new_node = Node(data)
                prev = curr.prev
                prev.next = new_node
                new_node.next = curr
                curr.prev = new_node
                new_node.prev = prev
                return
            curr = curr.next


    def delete(self, key):
        curr = self.head
        if curr is None:
            return

        while curr:
            # remove head onoe
            if curr == self.head:
                # if only head node exists
                if curr.next is None and curr.data == key:
                    self.head = None
                    curr = None
                    return
                elif curr.data == key:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
            else:
                # to remove any non - head node except last node
                if curr.next:
                    if curr.data == key:
                        nxt = curr.next
                        prev = curr.prev
                        prev.next = nxt
                        nxt.prev = prev
                        curr.prev = None
                        curr.next = None
                        curr = None
                        return
                else:
                    # remove last node
                    if curr.data == key:
                        prev = curr.prev
                        prev.next = None
                        curr.prev = None
                        curr = None
                        return
            curr = curr.next




    def add_after_node(self, key, data):
        curr = self.head
        while curr:
            if curr.next is None and curr.data == key:
                self.append(data)
                return
            elif curr.data == key:
                new = Node(data)
                next = curr.next
                curr.next = new
                new.next = next
                next.prev = new
                new.prev = curr
                return
            curr = curr.next


    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev



if __name__ == "__main__":
    dllist = DoubleLinkedList()
    dllist.append(1)
    dllist.append(2)
    dllist.append(3)
    dllist.append(4)
    dllist.print_list()
