def transpose(l):
    transposed_list=[]
    for i in range(len(l[0])):
        temp_list = []
        for j in range(len(l)):
            temp_list.append(l[j][i])
        transposed_list.append(temp_list)
    return transposed_list


print(transpose([[1,4,9]]))
print(transpose([[1,3,5],[2,4,6]]))
print(transpose([[1,1,1],[2,2,2],[3,3,3]]))
"""
00
01
02

00,10
01,11
02,12

00,10,20
01,11,21
02,12,22
"""