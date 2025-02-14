class TreeNode:
    """Tree Node definition"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary Tree with DFS Traversals"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert node into binary tree level-wise"""
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            temp = queue.pop(0)
            if not temp.left:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if not temp.right:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    # 1️⃣ Preorder Traversal (Root → Left → Right)
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # 2️⃣ Inorder Traversal (Left → Root → Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # 3️⃣ Postorder Traversal (Left → Right → Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

# 4️⃣ Taking User Input to Build Tree
tree = BinaryTree()
n = int(input("Enter number of nodes: "))
print(f"Enter {n} node values:")
for _ in range(n):
    tree.insert(int(input()))

# 5️⃣ Performing DFS Traversals
print("\nPreorder DFS:")
tree.preorder(tree.root)
print("\nInorder DFS:")
tree.inorder(tree.root)
print("\nPostorder DFS:")
tree.postorder(tree.root)
