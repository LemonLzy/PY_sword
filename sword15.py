# 二进制中1的个数：https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/

# 使用内置方法转为二进制，与'1'做判断计数
def hamming_weight(n: int) -> int:
    b = bin(n)[2:]
    count = int()
    for i in b:
        if i == '1':
            count += 1
    return count


# 位运算：与运算，一个数-1，与该数字做与运算，会将该整数的最右边的1变成0，有多少个1就可以做多少次这样的运算，从而统计出1的个数
def hamming_weight2(n: int) -> int:
    count = int()
    while n:
        count += 1
        n &= n - 1
    return count


if __name__ == '__main__':
    n = 11
    print(hamming_weight(n))
    print(hamming_weight2(n))
