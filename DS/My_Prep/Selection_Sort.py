"""T(n)=O(n**2)"""
def selection_sort(l):
    for start in range(len(l)):
        for i in range(start,len(l)):
            minpos = start
            if l[i]<l[minpos]:
                minpos=i
            l[start],l[minpos]=l[minpos],l[start]

    return l


l=[4,5,6,3,5]
print(selection_sort(l))