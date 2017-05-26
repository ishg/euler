a = 600851475143
b = 2
c = 0

while b <= a:
  if a % b is 0:
    a = a / b
    c = b
    b = 2
    print a, b, c
  else:
    b += 1

print c

# 6857
