def task_1() -> str:
    a: int = 7
    b: float = 3.12
    c: str = 'привет'
    d: list = [1, 2, 3]
    e: bool = True
    return a, type(a), b, type(b), c, type(c), d, type(d), e, type(e)


print (task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


print(task_2())
# 1, 2, 3, 5, 8, 13, 21 - последовательность чисел фибоначчи


def task_3() -> int:
    a: int = 7
    return a ** 2


print(task_3())


