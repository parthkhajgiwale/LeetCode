height = [1,7,2,5,4,7,3,6]
left = 0
right = len(height)-1
best = 0

while left < right:
  width = min(height[left], height[right])
  length = right - left
  product = width*length
  best = max(product, best)
  if height[left] < height[right]:
    left+=1
  else:
    right-=1
print(best)
