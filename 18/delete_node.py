from basic import ListNode, make_list_node, traversal_list_node


def delete_node(head: ListNode, val: int) -> ListNode:
    dummy = ListNode(-1)

    q = dummy
    p = head
    while p:
        if p.val != val:
            q.next = p
            q = q.next

        # 将下一个节点复制到当前节点，从而变相完成删除当前节点的操作
        temp = p.next
        p.next = None
        p = temp
    return dummy.next


if __name__ == '__main__':
    head = [4, 5, 1, 9]
    node = make_list_node(head)
    val = 5
    print(traversal_list_node(delete_node(node, val)))
