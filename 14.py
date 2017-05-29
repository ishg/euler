def createCollatzSeq(n):
  seq = []
  seq.append(n)
  while n > 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3 * n + 1
    seq.append(n)
  return seq

num, l = 0, 0
for i in range(1000000, 0, -1):
  x = len(createCollatzSeq(i))
  if x > l:
    l = x
    num = i

print num

# 837799