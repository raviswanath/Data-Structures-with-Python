# circular linked list implementation

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList():
    def __init__(self):
        self.head = None


    def apend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head


    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node


    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                break


    def remove(self, key):
        if self.head:
            if self.head.data == key:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    curr.next = self.head.next
                    self.head = self.head.next
            else:
                curr = self.head
                prev = None
                while curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == key:
                        prev.next = curr.next
                        curr = curr.next


    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count


    def split_list(self):
        length = len(self)

        if length == 0:
            return
        if length == 1:
            return self

        mid = length // 2
        count = 0
        prev = None
        curr = self.head

        while curr and count < mid:
            count += 1
            prev = curr
            curr = curr.next
        prev.next = self.head

        split_class = CircularLinkedList()
        while curr.next != self.head:
            split_class.apend(curr.data)
            curr = curr.next
        split_class.apend(curr.data)
        self.print_list()
        print("\n")
        split_class.print_list()


    def remove_node(self, node):
        if self.head == node:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            if self.head == self.head.next:
                self.head = None
            else:
                curr.next = self.head.next
                self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr == node:
                    prev.next = curr.next
                    curr = curr.next


    def josephus_circle(self, step):
        cur = self.head
        length = len(self)
        while length > 1:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
            print("Kill" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length -= 1



if __name__ == '__main__':
    cllist = CircularLinkedList()
    cllist.apend(1)
    cllist.apend(2)
    cllist.apend(3)
    cllist.apend(4)


    cllist.josephus_circle(5)
    cllist.print_list()
