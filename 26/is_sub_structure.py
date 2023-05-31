from basic import TreeNode, make_tree_node


def is_sub_structure(A: TreeNode, B: TreeNode) -> bool:
    res = bool()

    if A is not None and B is not None:
        if A.val == B.val:
            res = has_tree(A, B)
        # 注意后续条件必须使用if，不能使用elif，因为使用elif后就不会进入后续判断
        if not res:
            res = is_sub_structure(A.left, B)
        if not res:
            res = is_sub_structure(A.right, B)

    return res


def has_tree(p1: TreeNode, p2: TreeNode) -> bool:
    if p2 is None:
        return True

    if p1 is None:
        return False

    if p1.val != p2.val:
        return False

    # 此时p1.val == p2.val，所以需要递归地判断左右子数是否相同
    return has_tree(p1.left, p2.left) and has_tree(p1.right, p2.right)


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = [3]
    node_A = make_tree_node(A)
    node_B = make_tree_node(B)
    print(is_sub_structure(node_A, node_B))
