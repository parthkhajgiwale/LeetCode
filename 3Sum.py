nums=[2,4,8,9,10,6]
nums.sort
target = 12
res =[]

for i in range(len(nums)-2):
  left = i+1
  right = len(nums)-1
  while left < right:
    curr_sum = nums[i]+nums[left]+nums[right]
    if target == curr_sum:
      res.append([nums[i],nums[left],nums[right]])
      left+=1
      right-=1
    if curr_sum < target:
      left+=1
    else:
      right-=1
print(res)
