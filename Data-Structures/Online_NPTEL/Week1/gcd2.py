m=int(input('Enter First Number: '))
n=int(input('Enter Second Number: '))


for i in range(1,min(m,n)+1):
    if m%i==0 and n%i==0:
        gcd=i

print('GCD Value of',m,'and',n,'is:',gcd)