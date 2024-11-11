# Red Black Tree Visualizer

Start the program by running main.py. It first builds a red black tree containing the values specified in rbinput.txt. The values should be comma-separated without any spaces in between.

The user can then specify one of seven commands through the command line interface:

```insert [value]``` Adds the given number to the tree.

```delete [value]``` Finds the node with the given value in the tree and deletes it.

```search [value]``` Finds the node with the given value in the tree.

```sort``` Prints a list of all the values in the tree in sorted order by performing an inorder traversal of the tree.

```min``` Prints the minimum value in the tree.

```max``` Prints the maximum value in the tree.

```quit``` Exits the program.

A diagram of the current tree is stored in current_tree.png, and it is updated whenever changes are made to the tree.

The height of the tree is printed after each operation.
