limit = 4 * (10 ** 6)

def isEven(n):
  return n % 2 == 0
  
s = 0
mfib = 1
nfib = 2

while mfib < limit:
  if isEven(mfib):
    s+= mfib
  tmp = nfib
  nfib = mfib + nfib
  mfib = tmp
  
print s

# 4613732
