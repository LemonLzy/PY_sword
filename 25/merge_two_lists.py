from basic import ListNode, make_list_node, traversal_list_node


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    p = ListNode(None)
    head = p

    while l1 and l2:
        if l1.val <= l2.val:
            p.val = l1.val
            l1 = l1.next
        else:
            p.val = l2.val
            l2 = l2.next

        if l1 and l2:
            p.next = ListNode(None)
            p = p.next

    if l1:
        p.next = l1
    else:
        p.next = l2
    return head


if __name__ == '__main__':
    list1 = make_list_node([])
    list2 = make_list_node([])
    res = merge_two_lists(list1, list2)
    print(traversal_list_node(res))
