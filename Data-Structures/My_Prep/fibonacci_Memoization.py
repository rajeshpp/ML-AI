d={}
def fib(n):
    if d.get(n):
        return d[n]
    if n==0 or n==1:
        value=1
    else:
        value=fib(n-1)+fib(n-2)

    d[n]=value
    return value

print(fib(23))