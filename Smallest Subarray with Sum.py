arr = [2, 3, 1, 2, 4, 3]
S = 7

left = 0
window_sum = 0
min_length = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]

    while window_sum >= S:
        min_length = min(min_length, right - left + 1)
        window_sum -= arr[left]
        left += 1

print(0 if min_length == float('inf') else min_length)
