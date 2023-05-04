# 从尾到头打印链表：https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
from typing import List

from basic import ListNode


def reverse_print(head: ListNode) -> List[int]:
    # 遍历链表，放入栈中，后进先出
    res = list()
    p = head
    while p is not None:
        # 不建议使用insert方法，效率很低
        res.insert(0, p.val)
        p = p.next
    return res


def reverse_print2(head: ListNode) -> List[int]:
    # 递归实现，不建议使用递归，容易溢出
    while head is None:
        return []
    return reverse_print(head.next) + [head.val]


def reverse_print3(head: ListNode) -> List[int]:
    # 遍历链表，放入栈中，后进先出
    res = list()
    p = head
    while p is not None:
        res.append(p.val)
        p = p.next
    return res[::-1]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(2)

    print(reverse_print(head))
    print(reverse_print2(head))
    print(reverse_print3(head))
