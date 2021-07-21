from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_bt(value_queue):
    """create binary tree"""

    if len(value_queue) <= 0:
        return None, None

    root = Node(value_queue.popleft())

    current_queue = deque()
    current_queue.append(root)

    while len(current_queue) > 0 and len(value_queue) > 0:

        current_node = current_queue.popleft()

        left = value_queue.popleft()
        if left is not None:
            current_node.left = Node(left)
            current_queue.append(current_node.left)

        right = value_queue.popleft()
        if right is not None:
            current_node.right = Node(right)
            current_queue.append(current_node.right)

    return root


def create_bt_fls(value_list):
    """create binary create from list"""

    return create_bt(deque(value_list))


def lca_bst(bst, v1, v2):
    """lowest common ancestor of two nodes
       in a binary search tree"""

    if v1 <= bst.value <= v2 or v1 >= bst.value >= v2:
        return bst
    elif bst.value > v1 and bst.value > v2:
        return lca_bst(bst.left, v1, v2)
    else:
        return lca_bst(bst.right, v1, v2)


bt = create_bt_fls([6, 2, 8, 1, 3, 7, 9])
for _ in range(3) :
    first = int(input("input1 = "))
    second = int(input("input2 = "))
    lca = lca_bst(bt, first, second)
    print("answer :", lca.value)
    print("-----------------------------")