arr = [2,4,8,9,0,10,16]
target = 24

seen = {}

for i, num in enumerate(arr):
    difference = target - num
    
    if difference in seen:
        print(f"Match found at {seen[difference]} and {i}")
    
    seen[num]=i
