import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current % m, (previous + current) % m

    return current


n=int(input())
m=int(input())
print(get_fibonacci_huge_naive(n, m))