"""Longest Common Word"""
LCW=[]
def LCW(u,v):
    LCW=[[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
    maxLen=0
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                LCW[r][c]=1+LCW[r+1][c+1]
            else:
                LCW[r][c]=0
            if LCW[r][c]>maxLen:
                maxLen=LCW[r][c]
    return maxLen

str1=input("Enter String 1:")
str2=input("Enter String 2:")
print(LCW(str1,str2))