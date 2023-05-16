from typing import List


# 基础解法，使用位运算，拆分出奇数、偶数列表，然后拼接
def exchange(nums: List[int]) -> List[int]:
    # 奇数列表
    odd = list()
    # 偶数列表
    even = list()

    for i in nums:
        if i & 1 != 0:
            odd.append(i)
        else:
            even.append(i)

    return odd + even


# 基础解法二，双指针，可以将判断奇偶的部分抽取为独立函数，会变成一个更加通用的框架
def exchange2(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        # 当left指针所在值为奇数时，向右边移动，直到找到偶数
        while (left < right) and (nums[left] & 1 != 0):
            left += 1

        # 当right指针所在值为偶数时，向左边移动，直到找到奇数
        while (left < right) and (nums[right] & 1) == 0:
            right -= 1

        # 当左指针在右指针左边时，表示整个数组仍然需要移动，此时交换对应值的位置
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    return nums


if __name__ == '__main__':
    nums = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    print(exchange2(nums))
