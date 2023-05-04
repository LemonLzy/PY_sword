# 斐波那契数列：https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/

# 递归实现，容易溢出
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# 循环实现，不溢出
def fib2(n: int) -> int:
    if n == 0 or n == 1:
        return n

    x, y = 0, 1
    # 注意这里只需要遍历n
    for i in range(n):
        x, y = y, x + y
    return x % 1000000007


# 使用自底向上的动态规划完成，速度最快
def fib3(n: int) -> int:
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # 注意数组长度为n+1，防止越界，因为fib(5)实际上是指第六个数，所以数组需要存6个树，长度为n+1
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n] % 1000000007


if __name__ == '__main__':
    print(fib2(2))
    print(fib3(5))
