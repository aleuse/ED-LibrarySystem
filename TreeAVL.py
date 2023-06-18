import NodeAVL

class TreeAVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        sub_tree = new_root.left

        new_root.left = node
        node.right = sub_tree

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)) 
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rotate_right(self, node):
        new_root = node.left
        sub_tree = new_root.right

        new_root.right = node
        node.left = sub_tree

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def balance(self, node, value):
        if node is None:
            return NodeAVL(value)

        if value < node.value.name:
            node.left = self.balance(node.left, value)
        else:
            node.right = self.balance(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        _balance = self.get_balance(node)

        if _balance > 1:
            if value < node.left.value.name:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if _balance < -1:
            if value > node.right.value.name:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def insert(self, value):
        self.root = self.balance(self.root, value)
    
    def in_order(self):
        results = []
        def traverse(node):            
            if node.left is not None:
                traverse(node.left)
            results.append(node.value)
            if node.right is not None:
                traverse(node.right)
        traverse(self.root)
        return results