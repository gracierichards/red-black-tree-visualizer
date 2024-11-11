from rbtree import *
import matplotlib.pyplot as plt

# Example of building a tree without using the insert function
root = Node(value=96, p=Nil(), color=Color.BLACK)
node2 = root.addLeftChild(83, 1)
node3 = node2.addLeftChild(56, 0)
node4 = node3.addLeftChild(5, 1)
node5 = node4.addLeftChild(3, 0)
node6 = root.addRightChild(98, 1)
node7 = node4.addRightChild(37, 0)

# # Sort
# print(root.sort())

# # Search
# print("Searching for 37")
# result_node = root.search(37)
# if result_node:
#     print(result_node.value)
# else:
#     print(result_node)
# print("Searching for 7")
# result_node = root.search(7)
# if result_node:
#     print(result_node.value)
# else:
#     print(result_node)

# # Min and Max
# print(root.min().value)
# print(root.max().value)

# # Successor
# print("Successor of", root.value, "is", root.successor().value)
# print("Successor of", node2.value, "is", node2.successor().value)
# print("Successor of", node3.value, "is", node3.successor().value)
# print("Successor of", node4.value, "is", node4.successor().value)
# print("Successor of", node5.value, "is", node5.successor().value)
# print("Successor of", node6.value, "is", node6.successor().value)
# print("Sucessor of", node7.value, "is", node7.successor().value)

# # Predecessor
# print("Predecessor of", root.value, "is", root.predecessor().value)
# print("Predecessor of", node2.value, "is", node2.predecessor().value)
# print("Predecessor of", node3.value, "is", node3.predecessor().value)
# print("Predecessor of", node4.value, "is", node4.predecessor().value)
# print("Predecessor of", node5.value, "is", node5.predecessor().value)
# print("Predecessor of", node6.value, "is", node6.predecessor().value)
# print("Predecessor of", node7.value, "is", node7.predecessor().value)

# visualize(root)
# plt.show()

# # Insert (and rotate) test
# tree = RBTree()
# tree.insert(96)
# tree.insert(83)
# tree.insert(56)
# tree.insert(5)
# tree.insert(3)
# tree.insert(98)
# tree.insert(37)
# tree.insert(70)
# tree.insert(60)
# visualize(tree.root)
# plt.show()

# # Test 2
# tree = RBTree()
# tree.insert(11)
# tree.insert(2)
# tree.insert(14)
# tree.insert(1)
# tree.insert(7)
# tree.insert(15)
# tree.insert(6)
# tree.insert(8)
# tree.insert(4)
# tree.insert(16)
# tree.insert(17)
# tree.insert(3)
# tree.insert(5)
# visualize(tree.root)
# plt.show()

# Delete test
tree = RBTree()
tree.insert(11)
tree.insert(2)
tree.insert(14)
tree.insert(1)
tree.insert(7)
tree.insert(15)
tree.insert(6)
tree.delete_value(2)
tree.insert(8)
tree.insert(4)
tree.insert(16)
tree.delete_value(11)
tree.insert(17)
tree.insert(3)
tree.insert(5)
tree.delete_value(6)
visualize(tree.root)
plt.show()