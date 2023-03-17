'''
Task here: /src/tree_bin_iterative_changes/*.png
'''
from __future__ import annotations


class Node:
    def __init__(self, val: int, parent: Node = None, lchild: Node = None, rchild: Node = None, is_left: bool = True):
        self.val = val
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.is_left = is_left

    def __str__(self):
        # return f'parent: {self.parent}, val: {self.val}, lch: {self.lchild}, rch: {self.rchild}'
        return f'val: {self.val}'


def get_child_val(parent: int) -> (int, int):
    return 2*parent, 2*parent+1


def get_parent_val(child_val: int) -> (int, int):
    if child_val == 1:
        return 1, 0
    if child_val % 2 == 0:
        return int(child_val / 2), 0
    else:
        return int((child_val-1) / 2), 1


def tree_bin_iterative_changes(data: str) -> str:
    input_data_list = [[int(item) for item in line.split(' ')] for line in data.split('\n')]
    print(input_data_list)
    operations = input_data_list[1]
    tree = list(range(1, input_data_list[0][0]+1, 1))
    tree_n = {}
    for index, node_val in enumerate(tree):
        if index == 0:
            tree_n[node_val] = Node(val=node_val)
            continue
        potential_parent = get_parent_val(node_val)
        cur_parent = tree_n[potential_parent[0]]
        tree_n[node_val] = Node(val=node_val, parent=tree_n[potential_parent[0]])
        if potential_parent[1] == 0:
            cur_parent.lchild = tree_n[node_val]
        elif potential_parent[1] == 1:
            cur_parent.rchild = tree_n[node_val]
            tree_n[node_val].is_left = False

    print(tree_n.items())
    print(tree)
    print(operations)

    for node_to_change in operations:
        if tree_n[node_to_change].parent is None:
            continue
        # cur_val = node_to_change
        # parent_val = get_parent_val(cur_val)[0]
        # grandpa_val = get_parent_val(parent_val)[0]

        current = tree_n[node_to_change]
        # cur_parent = tree_n[parent_val]
        # cur_grandpa = tree_n[grandpa_val]

        # new_current = Node(val=cur_parent.val)
        # new_cur_parrent = Node(val=)
        if current.is_left:
            temp = current.rchild
            current.rchild = current
            current.parent.rchild = temp

        else:
            temp = current.lchild
            current.lchild = current
            current.parent.lchild = temp

        temp = current.parent
        current.parent = current.parent.parent
        temp.parent = current
        # if current.parent.parent is not None:
        #     if current.parent

        # cur_parent.parent = current
        # current.parent = cur_grandpa

    result_str = ''

    return result_str

'''
'7 10 5 2 8 4 9 1 6 3 \n'
'''
