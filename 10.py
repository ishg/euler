# Find sum of primes below number n

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

def findSumOfPrimesBelow(n):
  sum = 0
  for i in range(2, n):
    if isPrime(i):
      sum += i
      print i
  return sum

print findSumOfPrimesBelow(2000000)

# 142913828922