fin = open('data/input_13.txt', 'r')

numbers = []
for line in fin:
  numbers.append(int(line))

sum = 0
for i in range(len(numbers)):
  sum += numbers[i]

print str(sum)[:10]

# 5537376230