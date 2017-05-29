import math

def numOfDivisors(n):
  nod = 0
  sqrt = int(math.sqrt(n))
  for i in range(1, sqrt+1):
    if n % i == 0:
      nod += 2
  if sqrt * sqrt == n:
    nod -= 1

  return nod

i = 1
num = 0
while numOfDivisors(num) <= 500:
  num += i
  i += 1

print num

# 76576500
