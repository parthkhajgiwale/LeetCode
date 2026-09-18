arr = [1,1,2,2,3,3,4,4]
left = 0

for right in range(0,len(arr)):
  if arr[left]!=arr[right]:
    left+=1
    arr[left]=arr[right]
print(arr[:left+1])
