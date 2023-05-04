# 数值的整数次方：https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/

# 初级解法：未考虑负数
def my_pow(x: float, n: int) -> float:
    product = 1.0
    for i in range(n):
        product *= x
    return product


# 进阶：递归，位运算
def my_pow2(x: float, n: int) -> float:
    # 当n<0时，需要计算x在-n次方下的结果，然后求倒数
    return quick_mul(x, n) if n >= 0 else 1 / quick_mul(x, -n)


# 可以用如下公式计算a的n次方：
# a^n = a^(n/2) * a^(n/2)           n为偶数
# a^n = a^(n-1/2) * a^(n-1/2) * n   n为奇数
def quick_mul(x: float, n: int) -> float:
    # 指数为0时，结果均为1
    if n == 0:
        return 1
    # 指数为1时，结果均为x本身
    if n == 1:
        return x

    # 分治思想，每次求出n/2指数的情况
    product = my_pow2(x, n >> 1)
    product *= product

    # 如果指数是奇数，根据公式，则需要额外乘以x本身
    if (n & 0x1) == 1:
        product *= x
    return product


# TODO 快速幂：
#  https://leetcode.cn/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/jian-dan-li-jie-kuai-su-mi-by-ollieq-rl74/

if __name__ == '__main__':
    print(my_pow(4, -1))
    print(my_pow2(4, -2))

    print(3 >> 1)
    print(4 >> 1)
