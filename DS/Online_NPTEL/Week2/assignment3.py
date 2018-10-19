def sumprimes(list1):
    prime_list=[]
    for val in list1:
        if val>3:
            i,c=2,0
            while i<=(val//2):
                if val%i==0:
                   c=1
                i+=1
            if c==0:
                prime_list.append(val)
        elif val==2 or val==3:
            prime_list.append(val)
    sum=0
    for val in prime_list:
        sum+=val
    return sum

print(sumprimes([3,3,1,13]))
print(sumprimes([2,4,6,9,11]))
print(sumprimes([-3,1,6]))


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(round(x ** 0.5)) + 1, 2):
        if x % i == 0:
            return False
    else:
        return True

def sumprimes1(l):
    s=0
    for val in l:
        if val>1:
            if is_prime(val) == True:
                s+=0
    return s

print(sumprimes1([3,3,1,13]))
print(sumprimes1([2,4,6,9,11]))
print(sumprimes1([-3,1,6]))