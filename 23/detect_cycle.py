from basic import ListNode


def detect_cycle(head: ListNode) -> ListNode:
    # 判断是否存在环
    meeting_head = is_cycle(head)
    if meeting_head is None:
        return None

    # 计算环中节点的数量
    count = 1
    p = meeting_head
    while p != meeting_head:
        p = p.next
        count += 1

    # 再次定义双指针，第一个指针移动环中节点数量的步数，然后两个指针同时移动，当再次相遇时，则为环的起点
    p1, p2 = head, head
    for i in range(count):
        p1 = p1.next

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def is_cycle(head: ListNode) -> ListNode:
    fast, slow = head, head

    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return fast
    return None


if __name__ == '__main__':
    pass
