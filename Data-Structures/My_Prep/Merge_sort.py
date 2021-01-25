"""T(n)=O(n log n)"""
def merge(A,B):  #merge A[0:m], B[0:n]
    C,m,n,i,j=[],len(A),len(B),0,0  #i,j are current positions in A,B respectively

    while i+j<m+n:  #i+j is number of elements merged so far.

        if i==m:  #Case 1: A is Empty
            C.append(B[j])
            j+=1
        elif j==n:  #Case 2: B is Empty
            C.append(A[i])
            i+=1
        elif A[i]<=B[j]:  #Case 3: Head of A is Smaller
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:  #Case 4: Head of B is Smaller
            C.append(B[j])
            j+=1
    return C


def mergesort(A,left,right):
    if right-left<=1:
        return A[left:right]
    if right-left>1:
        mid=(left+right)//2
        L=mergesort(A,left,mid)
        R=mergesort(A,mid,right)
        return merge(L,R)

l=[3423,34534,3463456,56756,12342342,56756867,345634534]
print(mergesort(l,0,6))