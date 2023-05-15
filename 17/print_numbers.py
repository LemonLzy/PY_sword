from typing import List


# 初级解法：如果n过大，可能会溢出
def print_numbers(n: int) -> List[int]:
    res = list()

    for i in range(1, 10 ** n):
        res.append(i)

    return res


# 进阶，大数问题，使用字符串保存
def print_numbers2(n: int) -> List[int]:
    res = list()

    def dfs(x):
        if x == n:
            res.append(''.join(nums))
            return
        for i in range(10):
            nums[x] = str(i)
            dfs(x + 1)

    nums = [0] * n
    dfs(0)
    return res[1:]


if __name__ == '__main__':
    n = 3
    print(print_numbers2(n))
