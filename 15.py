# Wrote a recursive solution, but took about 4 hours

size = 20
paths = 1
 
for i in range(size):
  paths *= (2 * size) - i;
  paths /= i + 1;

print paths

# 137846528820