def isPrime(n):
  i = n - 1
  while i >= 2:
    if n % i is 0:
      return False
    i = i - 1
  return True

def findLowerPrimes(n):
  primes = []
  for i in range(2, n+1):
    if isPrime(i):
      primes.append(i)
  return primes

def getPower(n, f):
  i = 1
  tmp = f
  while f <= n:
    f = f * tmp    
    i += 1
  return tmp ** (i - 1)

def getLCM(n):
  lcm = 1
  for i in findLowerPrimes(n):
    lcm = getPower(n, i) * lcm
  return lcm

print getLCM(20)

# 232792560
