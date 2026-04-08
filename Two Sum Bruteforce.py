arr = [2,4,8,9,0,10,16]
target = 24
found = False
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print("Match Found at",i,"and",j)
            found = True
            break
        if found == True:
            break
