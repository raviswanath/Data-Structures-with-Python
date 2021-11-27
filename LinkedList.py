class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


    def pre_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete_node(self, key):

        # if this happens to be the head
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = 0
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None


    def delete_node_at_pos(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                self.head = curr_node.next
                curr_node = None
                return

            prev = None
            cont = 0
            while curr_node and pos != count:
                pos = curr_node
                curr_node = curr_node.next
                count +=1

            if curr_node is None:
                return

            prev_node.next = curr_node.next
            curr_node = None

    def length_of_list(self):
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count


    def swap_nodes_by_val(self, key1, key2):

        if key1 == key2:
            return

        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next


    def reverse_ll(self):
        curr = self.head
        prev = None
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev


    def merged_sort(self, ll):
        p = self.head
        q = ll.head
        s = None

        if not q and not p:
            return
        if not q:
            return p
        if not p:
            return q

        if p and q:
            if p.data <= q.data:
                s = p
                p = p.next
            else:
                s = q
                q = q.next
            new_head = s
            while p and q:
                if p.data <= q.data:
                    s.next = p
                    s = p
                    p = s.next
                else:
                    s.next = q
                    s = q
                    q = s.next
            if not p:
                s.next = q
            if not q:
                s.next = p
        self.head = new_head
        return self.head


    def remove_duplicates(self):
        curr_node = self.head
        prev_node = None
        values = dict()
        while curr_node:
            if curr_node.data in values:
                prev_node.next = curr_node.next
                curr_node = None
            else:
                values[curr_node.data] = 1
                prev_node = curr_node
            curr_node = prev_node.next


    def nth_from_last(self, n):
        length = self.length_of_list()
        curr_node = self.head
        stop = length - n + 1
        i = 1
        while i != stop:
            curr_node = curr_node.next
            i += 1
        return curr_node.data


    def count_occurances_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursive(node.next, data)
        else:
            return self.count_occurances_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None
