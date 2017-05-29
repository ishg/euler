
def byThree(n):
  return n % 3 == 0

def byFive(n):
  return n % 5 == 0

def getSum(n):
  s = 0
  for i in range(n):
    if byThree(i) or byFive(i):
      s += i
  return s

print getSum(1000)

# 233168      
