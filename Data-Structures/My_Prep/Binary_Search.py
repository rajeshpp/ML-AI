"""
Data structure	Array
Worst-case performance	O(log n)
Best-case performance	O(1)
Average-case performance	O(log n)
Worst-case space complexity	O(1)
"""

def binary_search(myItem, myList):
    found,bottom,top=False,0,len(myList)-1

    while bottom<=top and not found:
        mid=(top+bottom)//2
        if myList[mid]==myItem:
            found=True
        elif myList[mid]<myItem:
            bottom=mid+1
        else:
            top=mid-1
    return found


L=list(range(100))
item=int(input("Enter an Item you are searching for:"))
if binary_search(item,L):
    print("Item Found")
else:
    print("Item Not Found")