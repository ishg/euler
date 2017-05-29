n = 100
sumsquares = 0
for i in range(1, n+1):
  sumsquares += i ** 2

squaresum = 0
for i in range(1, n+1):
  squaresum += i
squaresum = (squaresum ** 2)

diff = squaresum - sumsquares

print diff

# 25164150
