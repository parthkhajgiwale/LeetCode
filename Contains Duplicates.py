arr = [2,4,3,3]

seen = set()

for i in range(0,len(arr)):
    if arr[i] in seen:
        print(True)
        break
    seen.add(arr[i])
