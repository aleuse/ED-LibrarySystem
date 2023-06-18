from NodeAVL import NodeAVL

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
        
    def insert(self, node, value):
        if self.root is None:
            node = NodeAVL(value)
            self.root = node
            return node
        
        if node is None:
            return NodeAVL(value)

        if value.name < node.value.name:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if value.name < node.left.value.name:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if value.name > node.right.value.name:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node
        
    def find_successor(self, node):
        while node.left:
            node = node.left        
        return node
    
    def delete(self, node, value):
        if node is None:
            return None

        if value.name < node.value.name:
            node.left = self.delete(node.left, value)
        elif value.name > node.value.name:
            node.right = self.delete(node.right, value)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                suc = self.find_successor(node.right)
                node.value = suc.value
                node.right = self.delete(node.right, suc.value)

        if not node :
            return None

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node
    
    def _in_order(self, node, results):
        if node:
            self._in_order(node.left, results)
            results.append(node.value)
            self._in_order(node.right, results)

    def in_order(self):
        results = []
        self._in_order(self.root, results)
        return results