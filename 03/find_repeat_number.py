# 数组中重复的数字：https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
from typing import List


# 空间、时间复杂度：O(N)
def find_repeat_number(nums: List[int]) -> int:
    # 用数组来实现简单的hash表
    # nums数组的值当作count数组的下标，nums数组出现的次数当作count数组的值
    count = [0] * len(nums)
    for i in nums:
        count[i] += 1
        # 当count数组的值>1时，表示出现两次及以上，可直接返回
        if count[i] > 1:
            return i
    return -1


# 空间、时间复杂度：O(N)
def find_repeat_number2(nums: List[int]) -> int:
    # 效率比第一种方法差
    # 通过字典来判断，key出现第二次时直接返回
    count = dict()
    for i in nums:
        if i in count.keys():
            return i
        count[i] = 1
    return -1


# 空间、时间复杂度：O(N)
def find_repeat_number3(nums: List[int]) -> int:
    # 通过集合来判断，key出现第二次时直接返回
    count = set()
    for i in nums:
        if i in count:
            return i
        count.add(i)
    return -1


# 空间复杂度O(1)、时间复杂度：O(N)
def find_repeat_number4(nums: List[int]) -> int:
    for i in range(len(nums)):
        while nums[i] != i:
            # 当前值不等于索引下标时，判断是否和索引为nums[i]的值相等，如果相等，则找到了重复的数字（因为该数字在当前下标和nums[i]下标都出现了）
            if nums[i] == nums[nums[i]]:
                return nums[i]

            # 交换索引位置的值，直到当前值=索引
            # 这一步需要重点注意：a,b = b,a 的原理是先暂存(c, d)，然后按左右顺序赋值给b,a
            # 因此，如果写为 nums[i], nums[nums[i]] = nums[nums[i]], nums[i]，那么nums[i]会被先赋值，之后nums[nums[i]]指向的元素会出错
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


# 空间复杂度O(1)、时间复杂度：O(N)
def find_repeat_number5(nums: List[int]) -> int:
    i = int()
    while i < len(nums):
        # 遍历数组，如果nums[i] = i，表明值已在索引位置，无需交换，判断下一个值
        if nums[i] == i:
            i += 1
            continue
        # 如果nums[i] == nums[nums[i]]，说明找到重复值
        if nums[i] == nums[nums[i]]:
            return nums[i]
        # 否则交换索引为i和索引为nums[i]元素的位置
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


# 如果不能原地修改数组，数字范围在1～n，空间复杂度O(1)、时间复杂度：O(NlogN)
def find_repeat_number6(nums: List[int]) -> int:
    left = 1
    right = len(nums) - 1
    while left <= right:
        # 将数组分为两部分，统计前半部分的数字数量
        mid = left + ((right - left) >> 1)
        count = count_nums(nums, left, mid)

        # 当左边界等于右边界，此时只有一个元素，如果该元素count>1则说明重复
        if left == right:
            if count > 1:
                return left
            else:
                break

        # 如果大于>(mid-left+1)，则说明重复数字在前半部份，缩小右边界
        if count > (mid - left + 1):
            right = mid
        else:
            # 反之，缩小左边界
            left = mid + 1
    return -1


def count_nums(nums: List, left: int, right: int) -> int:
    count = 0
    for i in nums:
        if left <= i <= right:
            count += 1
    return count


if __name__ == '__main__':
    nums = [1, 1, 2, 1, 4, 5, 6, 7, 8, 9]
    print(find_repeat_number(nums))
    print(find_repeat_number2(nums))
    print(find_repeat_number3(nums))
    print(find_repeat_number4(nums))
    print(find_repeat_number5(nums))
    print(find_repeat_number6(nums))


