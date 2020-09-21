
def last_digit_sum(n):

    if n<=1:
        return n

    prev, current, sum = 0,1,1

    for _ in range(n-1):

        prev,current = current, (prev+current)
        sum += current

    return sum%10

n = int(input())
print(last_digit_sum(n))

