class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        print("Duplicate key! Not inserted.")
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)


def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        # Node found
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children
        succ = get_successor(root)
        root.key = succ.key
        root.right = delete(root.right, succ.key)

    return root


# -------- MENU DRIVEN BST --------
root = None

while True:
    print("\n=== Binary Search Tree Menu ===")
    print("1. Insert Node")
    print("2. Delete Node")
    print("3. Search Node")
    print("4. Display (Inorder Traversal)")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key to insert: "))
        root = insert(root, key)
        print(f"Inserted {key} successfully!")

    elif choice == '2':
        if root is None:
            print("Tree is empty!")
        else:
            key = int(input("Enter key to delete: "))
            root = delete(root, key)
            print(f"Deleted {key} successfully!")

    elif choice == '3':
        if root is None:
            print("Tree is empty!")
        else:
            key = int(input("Enter key to search: "))
            if search(root, key):
                print(f"{key} found in the BST.")
            else:
                print(f"{key} not found in the BST.")

    elif choice == '4':
        if root is None:
            print("Tree is empty!")
        else:
            print("Inorder Traversal:")
            inorder(root)
            print()

    elif choice == '0':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")





Algorithm: Binary Search Tree Operations

Start the program.

Initialize root = None.

Display a menu with options: Insert, Delete, Search, Display, Exit.

If user selects Insert,
 • Take key input.
 • If tree is empty, create a new node as root.
 • Else, recursively find correct position and insert the node.

If user selects Delete,
 • Search for the key.
 • If found, delete the node using BST deletion rules (0, 1, or 2 children).

If user selects Search,
 • Recursively check whether the key exists in the BST.

If user selects Display,
 • Perform Inorder Traversal to show keys in ascending order.

Repeat steps 3–7 until Exit is chosen.

Stop the program.
