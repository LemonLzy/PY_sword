# Todo 青蛙跳台阶问题：https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
# 同：https://leetcode.cn/problems/climbing-stairs/
def num_ways(n: int) -> int:
    # if条件为了快速返回，也避免当n为0时，后续的dp赋值溢出
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n]


if __name__ == '__main__':
    n = 7
    print(num_ways(n))
