def approx_sin(x: float, n: int):
    sign = 1
    result = x
    tmp = x
    for i in range(1, n + 1):
        sign = -sign
        tmp = tmp * x * x
        tmp = tmp / ((2 * i) * (2 * i + 1))
        result += sign * tmp
    print(result)


def approx_cos(x: float, n: int):
    sign = 1
    result = 1
    tmp = 1
    for i in range(1, n + 1):
        sign = -sign
        tmp = tmp * x * x
        tmp = tmp / ((2 * i - 1) * (2 * i))
        result += sign * tmp
    print(result)


def approx_sinh(x: float, n: int):
    result = x
    tmp = x
    for i in range(1, n + 1):
        tmp = tmp * x * x
        tmp = tmp / ((2 * i) * (2 * i + 1))
        result += tmp
    print(result)


def approx_cosh(x: float, n: int):
    result = 1
    tmp = 1
    for i in range(1, n + 1):
        tmp = tmp * x * x
        tmp = tmp / ((2 * i - 1) * (2 * i))
        result += tmp
    print(result)


# Unit test
if __name__ == '__main__':
    approx_sin(x=3.14, n=10)
    approx_cos(x=3.14, n=10)
    approx_sinh(x=3.14, n=10)
    approx_cosh(x=3.14, n=10)
    approx_cosh(x=1, n=10)