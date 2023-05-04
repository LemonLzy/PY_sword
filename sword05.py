# 替换空格：https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
from typing import List


def replace_space(s: str) -> str:
    return "%20".join(s.split(" "))


def replace_space2(s: str) -> str:
    s = list(s)
    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "%20"
    return "".join(s)


def replace_space3(s: str) -> str:
    res = list()
    for i in s:
        if i == " ":
            res.append("%20")
        else:
            res.append(i)
    return "".join(res)


# python中字符串是不可变的，其他语言中字符串可能是可变的，所以可以原地修改，O(1)的空间复杂度
def replace_space4(s: str) -> str:
    pass


# Todo 进阶：合并数组：https://leetcode.cn/problems/merge-sorted-array/
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """


if __name__ == '__main__':
    s = "We are happy."
    print(replace_space(s))
    print(replace_space2(s))
    print(replace_space3(s))

    s = "     "
    print(replace_space(s))
    print(replace_space2(s))
    print(replace_space3(s))
