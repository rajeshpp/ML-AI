"""T(n)=O(n**2)"""
def insertion_sort(l):
    for sliceEnd in range(len(l)):
        pos=sliceEnd
        while pos>0 and l[pos]<l[pos-1]:
            l[pos],l[pos-1]=l[pos-1],l[pos]
            pos-=1
    return l


l=[4,5,6,3,5]
print(insertion_sort(l))