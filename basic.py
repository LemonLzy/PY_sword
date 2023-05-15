from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_tree(l: List) -> TreeNode:
    """ 由输入列表生成树，返回根节点 """
    q = []
    root = TreeNode(val=l.pop(0))
    q.append(root)
    while q:
        t = q.pop(0)
        if l:
            if l[0] != 'null':
                t.left = TreeNode(val=l.pop(0))
                q.append(t.left)
            else:
                l.pop(0)
        if l:
            if l[0] != 'null':
                t.right = TreeNode(val=l.pop(0))
                q.append(t.right)
            else:
                l.pop(0)
    return root


def make_list_node(head: list) -> ListNode:
    """
    根据列表，生成ListNode
    :param head: 列表
    :return: 根据列表生成的ListNode
    """
    p = ListNode(None)
    h = p
    for i in range(len(head)):
        p.val = head[i]
        if i == len(head) - 1:
            return h
        p.next = ListNode(None)
        p = p.next
    return h


def traversal_list_node(head: ListNode) -> list:
    res = list()

    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next

    return res
