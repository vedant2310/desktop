class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def insert(root, key):
    if root is None:
        return Node(key)
    if root.key == key:
        return root
    if root.key < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def del_node(root, x):
    if root is None:
        return root

    if root.key > x:
        root.left = del_node(root.left, x)
    elif root.key < x:
        root.right = del_node(root.right, x)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)

    return root


if __name__ == "__main__":
    root = Node(88)
    root = insert(root, 64)
    root = insert(root, 92)
    root = insert(root, 52)
    root = insert(root, 71)
    root = insert(root, 90)
    root = insert(root, 41)
    root = insert(root, 62)
    root = insert(root, 83)

    print("Inorder before deletion:")
    inorder(root)
    print()

    x = 64
    root = del_node(root, x)

    print(f"\nInorder after deleting {x}:")
    inorder(root)
    print()

    input("\nPress Enter to exit...") 
