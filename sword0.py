# 把一个字符串转换成整数
# Todo 考虑输入字符串有非数字字符和正负号，要考虑到最大的正整数和最小的负整数以及溢出，以及不能转换时的错误错误，以及类型错误时程序崩溃
def str_to_int(s: str) -> int:
    if not s.isdigit():
        print(f"{s} is not a digital.")
        return 0
    return int(s)


if __name__ == '__main__':
    s = "-1"
    print(str_to_int(s))
    s = "abc"
    print(str_to_int(s))
    s = "10000000000"
    print(str_to_int(s))
    s = None
    print(str_to_int(s))
