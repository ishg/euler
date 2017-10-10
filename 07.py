import math

def isPrime(n):
  if n is 2:
    return True
  elif n % 2 is 0:
    return False
  i = 3
  range = int(math.sqrt(n)) + 1
  while i < range:
    if n % i is 0:
      return False
    i += 1
  return True

def getNthPrime(index):
  i = 1
  p = 3
  while i < index:
    if isPrime(p):
      i += 1
    p += 2
  return p - 2

print getNthPrime(10001)

# 104743