class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)

        return self

    def delete(self, value):
        if (value < self.value):
            self.left = self.left.delete(value)
        elif (value > self.value):
            self.right = self.right.delete(value)
        else:
            if self.left is None:
                newnode = self.right
                self = None
                return newnode
            elif self.right is None:
                newnode = self.left
                self = None
                return newnode

            newnode = self.right.getMinimum()
            self.value = newnode
            self.right = self.right.delete(newnode)

        return self

    def getMinimum(self):
        minElement = self

        while (minElement.left is not None):
            minElement = minElement.left

        return minElement.value

    def getMaximum(self):
        maxElement = self

        while (maxElement.right is not None):
            maxElement = maxElement.right

        return maxElement.value

    def height(self):
        left_h = 0
        right_h = 0

        if self.left is not None:
            left_h = self.left.height()
        if self.right is not None:
            right_h = self.right.height()

        if left_h > right_h:
            return left_h + 1
        else:
            return right_h + 1


    def size(self):
        if (self.right is not None and self.left is not None):
            return self.left.size() + 1 + self.right.size()
        elif (self.right is not None):
            return 1 + self.right.size()
        elif (self.left is not None):
            return 1 + self.left.size()
        else:
            return 1

    def inorder(self):
        if self.value is not None:
            if self.left is not None:
                self.left.inorder()
            print(self.value, end=" ")
            print(" ", end=" ")
            if self.right is not None:
                self.right.inorder()

    def __str__(self):
        if self.value is not None:
            tree_size = self.size()
            print("The size of the binary tree is: ", tree_size)
            print("Binary Tree: ", end=" ")
            str(self.inorder())
            return " "

tree = BST(3)
tree.insert(2)
tree.insert(4)
print(tree)
print("Binary Tree Height: ", end=" ")
print(tree.height())
print("Binary Tree Minimum: ", end=" ")
print(tree.getMinimum())
print("Binary Tree Maximum: ", end=" ")
print(tree.getMaximum(), "\n")

tree = BST(5)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(7)
tree.insert(8)
tree.insert(6)

print(tree)
print("Binary Tree Height: ", end=" ")
print(tree.height())
print("Binary Tree Minimum: ", end=" ")
print(tree.getMinimum())
print("Binary Tree Maximum: ", end=" ")
print(tree.getMaximum(), "\n")

tree.delete(7)
print("After deleting the node 7...")
print(tree)
print(" ")

tree.delete(5)
print("After deleting the node 5...")
print(tree)
print(" ")

tree.delete(6)
print("After deleting the node 6...")
print(tree)
print(" ")
