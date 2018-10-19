"""T(n)=Worst Case: if pivot is max or min then : O(n**2)
        Average Case: Choose pivot randomly then: O(n log n)

        Note: Quicksort is very effecient, if the input is randomized.


        =========
Worst-case space complexity: O(n) auxiliary (naive); O(log n) auxiliary (Sedgewick 1978)
Worst-case performance: O(n2)
Best-case performance: O(n log n)
Average performance: O(n log n)

            """
import sys,random
sys.setrecursionlimit(10000)
def quick_sort(A,l,r):  #Sort A[l:r]
    if r-l<=1:  #Base Case
        return ()

    #Partition w.r.t pivot, A[l]
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            A[yellow],A[green]=A[green],A[yellow]
            yellow+=1

    #Move pivot into place
    A[l],A[yellow-1]=A[yellow-1],A[l]

    #Recursive Calls
    quick_sort(A,l,yellow-1)
    quick_sort(A,yellow,r)

def randomize(l):
    for i in range(len(l)//2):
        j=random.randrange(0,len(l),1)
        k=random.randrange(0, len(l), 1)
        l[j],l[k]=l[k],l[j]


l=list(range(10000,0,-1))
randomize(l)  #This helps to speedup the quicksort.
quick_sort(l,0,len(l))
print(l)