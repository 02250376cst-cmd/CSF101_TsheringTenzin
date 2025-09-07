print("hello world")
x = 2
y = 5
sum = x+y
print("The sum of x and y is: ",sum)
name = input("enter your name: ")
age = input("enter your age: ")
print("you are", name, "and you are", age, "years old")

class BinarySearchTree:
    # ... (previous code)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())
