from __future__ import annotations
from typing import Generator, List


def fib(n: int) -> List[int]:
    if not isinstance(n, int):
        raise TypeError("n должен быть целым числом")
    if n < 0:
        raise ValueError("n должен быть неотрицательным")

    if n == 0:
        return [0]
    seq = [0, 1]
    for _ in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq


def fib_gen(n: int):
    if not isinstance(n, int):
        raise TypeError("n должен быть целым числом")
    if n < 0:
        raise ValueError("n должен быть неотрицательным")

    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b




def _selftest() -> None:
    assert fib(0) == [0]
    assert fib(1) == [0, 1]
    assert fib(5) == [0, 1, 1, 2, 3, 5]
    assert list(fib_gen(0)) == [0]
    assert list(fib_gen(1)) == [0, 1]
    assert list(fib_gen(5)) == [0, 1, 1, 2, 3, 5]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fibonacci")
    parser.add_argument("n", type=int, help="Индекс n (>=0)")
    parser.add_argument("--gen", action="store_true", help="использовать генератор fib_gen")
    args = parser.parse_args()

    if args.gen:
        print(list(fib_gen(args.n)))
    else:
        print(fib(args.n))
