from rbtree import *
import sys

# Reads input that is a comma-separated list of values
input_file = open("Problem2/rbinput.txt", "r")
input_array = input_file.readline().split(',')
tree = RBTree()
for val in input_array:
    tree.insert(int(val))

fig = visualize(tree.root)
fig.savefig("Problem2/current_tree.png")

print("The available commands are:\ninsert [value]\ndelete [value]\nsearch [value]\nsort\nmin\nmax\nsuccessor [value]\npredecessor [value]\nleft-child [value]\nright-child [value]\nquit\n")
command = input("Please enter a command: ")
command_word = command.split()[0]
while command_word != "quit":
    match command_word:
        case "insert":
            val = command.split()[1]
            tree.insert(int(val))
            print("Inserted successfully.")
        case "delete":
            val = command.split()[1]
            tree.delete_value(int(val))
            print("Deleted successfully.")
        case "search":
            val = command.split()[1]
            found_node = tree.search(int(val))
            if found_node:
                print("Node is in tree.")
            else:
                print("Node is not in the tree.")
        case "sort":
            print("The elements of the tree in sorted order are", tree.sort())
        case "min":
            print("The minimum value in the tree is", tree.root.min().value)
        case "max":
            print("The maximum value in the tree is", tree.root.max().value)
        case "successor":
            val = command.split()[1]
            specified_node = tree.search(int(val))
            print("The successor of", val, "is", specified_node.successor().value)
        case "predecessor":
            val = command.split()[1]
            specified_node = tree.search(int(val))
            print("The predecessor of", val, "is", specified_node.predecessor().value)
        case "left-child":
            val = command.split()[1]
            specified_node = tree.search(int(val))
            print("The left child of", val, "is", specified_node.left.value)
        case "right-child":
            val = command.split()[1]
            specified_node = tree.search(int(val))
            print("The right child of", val, "is", specified_node.right.value)
        case _:
            print("Does not match any valid command. ")
    print("The height of the tree is", tree.height())
    fig = visualize(tree.root)
    print(fig)
    if fig:
        fig.savefig("Problem2/current_tree.png")
    else:
        print("Duplicate value. Not updating figure.")
    command = input("Please enter a command: ")
    command_word = command.split()[0]