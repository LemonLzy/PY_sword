from basic import ListNode, make_list_node, traversal_list_node


def reverse_list(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    last = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return last


def reverse_list2(head: ListNode) -> ListNode:
    # cur指向头节点，pre指向None
    cur, pre = head, None
    while cur:
        # 暂存后续节点
        tmp = cur.next
        # 修改当前节点的引用，箭头方向调换
        cur.next = pre
        # 移动pre的位置到当前节点
        pre = cur
        # 移动cur的位置到下一个节点
        cur = tmp
    return pre


if __name__ == '__main__':
    node = make_list_node([1, 2, 3, 4, 5])
    list_node = traversal_list_node(reverse_list(node))
    print(list_node)
