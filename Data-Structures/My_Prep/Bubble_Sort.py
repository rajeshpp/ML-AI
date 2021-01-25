"""
Complexity:
Worst-case space complexity: auxiliary
Best-case performance: О(n) comparisons, О(1) swaps
Worst-case performance: О(n2) comparisons, О(n2) swaps
Average performance: О(n2) comparisons, О(n2) swaps
"""

def bubblesort(myList):
    moreSwaps=True
    while moreSwaps:
        moreSwaps=False
        for element in range(len(myList)-1):
            if myList[element]>myList[element+1]:
                moreSwaps=True
                myList[element],myList[element+1]=myList[element+1],myList[element]

    return myList

l=[23,45,23,2,8,6,234,234234,34567]
print(bubblesort(l))