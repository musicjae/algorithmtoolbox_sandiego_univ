import sys
import builtins
def get_last_digit_naive(n):
    if n <= 1:
        return n

    prev = 0  # First F-number is 0
    current = 1  # Second F-number is 1

    for _ in range(n-1):
        prev, current = current, current + prev

    return current % 10

def get_last_digit_faster(n):

    if n<=1:
        return n

    prev,current = 0,1

    for _ in range(n-1):
        prev, current = current%10, (current+prev) % 10

    return current




if __name__ == '__main__':
    n = int(input())
    print(get_last_digit_faster(n))
