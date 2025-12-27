class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(arr):
    """
    Build binary tree from level-order array.
    Example: [1,2,3,4,5]
    """
    if not arr:
        return None

    nodes = [Node(v) if v is not None else None for v in arr]
    root = nodes[0]
    i = 1

    for node in nodes:
        if node:
            if i < len(nodes):
                node.left = nodes[i]
                i += 1
            if i < len(nodes):
                node.right = nodes[i]
                i += 1

    return root


def inorder(root, steps):
    if root:
        inorder(root.left, steps)
        steps.append(root.value)
        inorder(root.right, steps)


def preorder(root, steps):
    if root:
        steps.append(root.value)
        preorder(root.left, steps)
        preorder(root.right, steps)


def postorder(root, steps):
    if root:
        postorder(root.left, steps)
        postorder(root.right, steps)
        steps.append(root.value)