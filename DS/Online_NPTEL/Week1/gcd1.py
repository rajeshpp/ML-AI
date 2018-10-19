m=int(input('Enter First Number: '))
n=int(input('Enter Second Number: '))

print("Now getting first number factors....")
fm=[i for i in range(1,m+1) if m%i==0]
print(fm)

print("Now getting Second number factors....")
fn=[i for i in range(1,n+1) if n%i==0]
print(fn)

common=[]

for val in fm:
    if val in fn:
        common.append(val)


print('GCD Value of',m,'and',n,'is:',common[-1])