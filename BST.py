# Binary search tree implementation

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        return self.insert_helper(self.root, value)

    def search(self, value):
        return self.search_helper(self.root, value)

    def insert_helper(self, current, value):
        if current.data < value:
            if current.right:
                self.insert_helper(current.right, value)
            else:
                current.right = Node(value)
        else:
            if current.left:
                self.insert_helper(current.left, value)
            else:
                current.left = Node(value)

    def search_helper(self, current, value):
        if current:
            if current.data == value:
                return True
            elif current.data < value:
                return self.search_helper(current.right, value)
            elif current.data > value:
                return self.search_helper(current.left, value)


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(25)
    bst.insert(9)
    bst.insert(13)

    print(bst.search(9))
    print(bst.search(14))
