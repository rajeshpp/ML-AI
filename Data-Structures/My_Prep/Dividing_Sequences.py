n=int(input())
ar=[]

temp=0
for i in range (0,n):
    temp=int(input())
    ar.append(temp)

def best(i):
    if i==0:
        return (1)
    else:
        ans =1
        for j in range (0,i):
            if (ar[i]%ar[j]==0):
                ans=max(ans,(best(j)+1))
        return ans
an=[]
for i in range (0,n):
   temp=best(i)
   an.append(temp)

print(max(an))

