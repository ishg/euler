def isPal(n):
  s = str(n)
  for i in range(len(s)):
    if s[i] != s[len(s) - i - 1]:
      return False
  return True

n = 999
m = 99
pal = 0

while n > m:
  for i in range(n, m, -1):
    if isPal(n * i) and (n * i) > pal:
      pal = n * i
      break
  n = n-1

print pal

# 906609
