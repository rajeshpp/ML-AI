def linear_search(item,List):
    found=False
    for i in range(1,len(List)):
        if List[i]==item and found==False:
            found=True
            position=i
    return position


List=[2,3,4,6,634,234,234,5345,234,235,234,342,546]
item=int(input("Enter a value to Search from the list:"))
print('Item: {0} found at {1} position from the list {2} by using Linear Search'.format(item,linear_search(item,List),List))