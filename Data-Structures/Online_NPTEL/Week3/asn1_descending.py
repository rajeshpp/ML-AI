def descending(l):
    if len(l)==0:
        return True
    elif len(l)==1:
        return True
    else:
        for i in range(1,len(l)):
            if l[i-1]<l[i]:
                return False
    return True



print(descending([]))
print(descending([4,4,3]))
print(descending([19,17,18,7]))