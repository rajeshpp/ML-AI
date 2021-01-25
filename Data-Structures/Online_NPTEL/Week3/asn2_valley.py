def valley(list):
  if(len(list)==0):
    return(True)
  if(len(list)==1):
    return(False)
  if(list[0]<list[1]):
    return(False)
  for i in range(0,len(list)-1):
    if(list[i]<list[i+1]):
      pos=i
      break
    if(list[i]==list[i+1]):
      return(False)
  else:
    return(False)
  for i in range(pos,len(list)-1):
    if(list[i]>=list[i+1]):
      return(False)
  return(True)

print(valley([3,2,1,2,3]))
print(valley([3,2,1]))
print(valley([3,3,2,1,2]))
print(valley([2]))           #False
print(valley([13,12,14,14]))  #False
print(valley([5,4,3,2,1,2])) #True
print(valley([17,1,2,3,4,5]))  #True