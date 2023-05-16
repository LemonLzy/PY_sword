from basic import ListNode, make_list_node, traversal_list_node


# 基础解法：遍历出链表的深度，然后再次遍历到 n-k+1 的位置停止，即为倒数第K个节点
def get_kth_from_end(head: ListNode, k: int) -> ListNode:
    cur = head

    deep = int()
    while cur:
        cur = cur.next
        deep += 1

    count = int()
    while head:
        count += 1
        if count == (deep - k + 1):
            break
        head = head.next

    return head


# 进阶解法：双指针，第一个指针移动到k-1的位置，然后和第二个指针一起移动，当第一个指针到末尾时，第二个指针的位置即为倒数第K个节点
def get_kth_from_end2(head: ListNode, k: int) -> ListNode:
    p = head
    for i in range(k):
        p = p.next

    q = head
    while p:
        p = p.next
        q = q.next
    return q


# 进阶解法：增加鲁棒性
# 考虑链表为空、k为0、k超出链表长度的情况
def get_kth_from_end3(head: ListNode, k: int) -> ListNode:
    if head is None or k == 0:
        return None

    p = head
    for i in range(k):
        if p.next is not None:
            p = p.next
        else:
            return None

    q = head
    while p:
        p = p.next
        q = q.next
    return q


if __name__ == '__main__':
    node = make_list_node([1, 2, 3, 4, 5])
    print(traversal_list_node(get_kth_from_end(node, 6)))
    print(traversal_list_node(get_kth_from_end2(node, 2)))
