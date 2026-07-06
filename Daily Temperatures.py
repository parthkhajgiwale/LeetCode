temperatures = [30,38,36,35,40]
stack = []
result = [0]*len(temperatures)

for i,temp in enumerate(temperatures):
  while stack and temperatures[stack[-1]] < temp:
    prev = stack.pop()
    result[prev] = i - prev
  stack.append(i)

print(result)
