# Given a + b + c = 1000
# Find a, b, c for which a^2 + b^2 = c^2

def triplets(s):
  a = 0
  b = 0
  c = 0
  for a in range(s/3):
    for b in range(a, s/2):
      c = s - a - b
      if a * a + b * b == c * c:
        return a * b * c

print triplets(1000)

# 200, 375, 425
# 31875000
