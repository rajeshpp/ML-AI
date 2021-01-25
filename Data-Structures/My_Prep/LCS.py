"""Longest Common Subsequence"""
LCS=[]
def LCS(u,v):
    LCS=[[0 for i in range(len(v)+1)] for j in range(len(u)+1)]
    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                LCS[r][c]=1+LCS[r+1][c+1]
            else:
                LCS[r][c]=max(LCS[r+1][c],LCS[r][c+1])
    return LCS[0][0]

str1=input("Enter String 1:")
str2=input("Enter String 2:")
print(LCS(str1,str2))