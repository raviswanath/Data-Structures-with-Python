import Queue as q
import Stacks as s

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
       
        
    def search(self, node, key):
        # Base case: if the root is non existant or if the key is stored in root
        # return root node
        if node is None or node.value == key:
            return node
        # If the value in node is greater than key, search the left tree
        elif node.value > key:
            return self.search(node.left, key)
        # If the key is greater than node value, search the right sub tree
        elif node.value < key:
            return self.search(node.right, key)
     
    
    def insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                return self.insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                return self.insert(node.right, value)


    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal


    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal


    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = q.Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += (str(queue.peek()) + "-")
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        stack = s.Stack()
        queue = q.Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += (str(node.value) + "-")
        return traversal


    def print_tree(self, kind):
        if kind == "preorder":
            return self.preorder_print(tree.root, "")
        elif kind == "inorder":
            return self.inorder_print(tree.root, "")
        elif kind == "postorder":
            return self.postorder_print(tree.root, "")
        elif kind == "levelorder":
            return self.levelorder_print(tree.root)
        elif kind == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Invalid traversal type.")
            return False


    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)


if __name__ == "__main__":
    tree = BinaryTree(3)
    tree.root.left = Node(2)
    tree.root.right = Node(4)
    tree.root.left.left = Node(1)
    tree.root.right.right = Node(5)

    print(tree.size_(tree.root))
