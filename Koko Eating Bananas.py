import math
piles = [25,10,23,4]
h = 4
left = 1
right = max(piles)

while left < right:
  k=(left+right)//2

  hours = 0
  for pile in piles:
    hours+=math.ceil(pile/k)
  
  if hours<=h:
    right=k
  if hours>h:
    left=k+1
print(left)

