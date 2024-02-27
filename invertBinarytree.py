class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self, node=None, results=[]): 
        node = node or self.root
        if node:
            self.in_order(node.left, results) 
            results.append(node.value)
            self.in_order(node.right, results)
        return results

    def pre_order(self, node=None, results=[]):
        node = node or self.root
        if node:
            results.append(node.value)
            self.pre_order(node.left, results)
            self.pre_order(node.right, results)
        return results

    def post_order(self, node=None, results=[]):
        node = node or self.root
        if node:
            self.post_order(node.left, results)
            self.post_order(node.right, results)
            results.append(node.value)
        return results

    def find_max_val(self, root):
        if not root:
            return None

        max_val = root.value
        left_val = self.find_max_val(root.left)
        right_val = self.find_max_val(root.right)

        if left_val:  
            max_val = max(max_val, left_val)
        if right_val: 
            max_val = max(max_val, right_val)

        return max_val

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    break

    def contains(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def __str__(self): 
        def print_tree(node, level):
            if node:
                print_tree(node.right, level + 1)
                print(' ' * 4 * level + str(node.value))
                print_tree(node.left, level + 1)

        output = ""
        print_tree(self.root, 0)
        return output


tree = BinarySearchTree()
tree.add(10)
tree.add(5)
tree.add(9)
tree.add(50)
tree.add(55)

print(tree)