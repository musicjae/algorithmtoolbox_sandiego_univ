import sys
import builtins

def gcd_naive (a,b):


    current_gcd=1

    for d in range(2,min(a,b)+1):
        if(a%d==0 & b%d==0):
            if current_gcd < d:
                current_gcd = d

    return d

def gcd_euclid (m,n):

    a = max(m,n)
    b = min(m,n)

    while b != 0:

        r = a % b
        a = b
        b = r

    return a

if __name__ == "__main__":

    a= int(input())
    b=int(input())

    print(gcd_euclid(a,b))



