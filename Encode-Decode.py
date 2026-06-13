#encoder
str_list = ["Hello World", "Python"]
encoded=[]
for s in str_list:
  encoded.append(f"{len(s)}#{s}")
s=''.join(encoded)
s

#decoder
res = []
i=0
while i<len(s):
  j=i
  while s[j]!='#':
    j+=1
  length = int(s[i:j])
  word = s[j+1:j+1+length]
  res.append(word)
  i = j+1+length
res
