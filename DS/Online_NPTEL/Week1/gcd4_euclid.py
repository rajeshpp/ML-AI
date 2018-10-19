m=int(input('Enter First Number: '))
n=int(input('Enter Second Number: '))

"""Both of the below will take same number of steps"""
"""Recursion won't work for highest numbers and it fails with RecursionError"""
def gcd_with_recursion(m,n):
    if m%n==0:
        return n
    else:
        return gcd_with_recursion(n,m-n)

def gcd_without_recursion(m,n):
    while m%n!=0:
        diff=m-n
        m,n=max(n,diff), min(n,diff)
    return n


if m>=n:
    print('GCD Value of', m, 'and', n, 'with recursion is:', gcd_with_recursion(m, n))
    print('GCD Value of', m, 'and', n, 'without recursion is:', gcd_without_recursion(m, n))
else:
    print('GCD Value of', m, 'and', n, 'with recursion is:', gcd_with_recursion(n, m))
    print('GCD Value of', m, 'and', n, 'without recursion is:', gcd_without_recursion(n, m))