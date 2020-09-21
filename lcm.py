import gcd

def lcm(a,b):

    return (a*b)/gcd.gcd_euclid(a,b)

a=int(input())
b=int(input())
print(int(lcm(a,b)))



