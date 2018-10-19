m=int(input('Enter First Number: '))
n=int(input('Enter Second Number: '))


"""This is the original algorithm proposed by Euclid and this is very very efficient."""
def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)

if m>=n:
    print('GCD Value of', m, 'and', n, 'with recursion is:', gcd(m, n))
else:
    print('GCD Value of', m, 'and', n, 'with recursion is:', gcd(n, m))


