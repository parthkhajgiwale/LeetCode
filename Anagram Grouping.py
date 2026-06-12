def anagrams(str):
  groups = {}
  for word in str:
    count = [0]*26
    for ch in word:
      count[ord('a')-ord(ch)]+=1
    key = tuple(count)

    if key not in groups:
      groups[key] = []
    
    groups[key].append(word)
  return list(groups.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(anagrams(strs))
