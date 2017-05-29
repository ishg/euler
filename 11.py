w, h = 20, 20
matrix = [[0 for x in range(w)] for y in range(h)]

def getWords(line):
  words = []
  word = ''
  for i in range(len(line)):
    if line[i] == ' ':
      words.append(word)
      word = ''
    else:
      word += line[i]
  return words

fin = open('data/input_11.txt', 'r')

i = 0
for line in fin:
  j = 0
  for word in getWords(line):
    matrix[i][j] = int(word)
    j += 1
  i += 1

fin.close()

def checkTop(row, col):
  product = 1
  for i in range(4):
    if row - i > 0:
      product = product * matrix[row - i][col]
  return product

def checkBot(row, col):
  product = 1
  for i in range(4):
    if row + i < 20:
      product = product * matrix[row + i][col]
  return product

def checkLeft(row, col):
  product = 1
  for i in range(4):
    if col - i > 0:
      product = product * matrix[row][col -i]
  return product

def checkRight(row, col):
  product = 1
  for i in range(4):
    if col + i < 20:
      product = product * matrix[row][col + i]
  return product

def topLeft(row, col):
  product = 1
  for i in range(4):
    if row - i > 0 and col - i > 0:
      product = product * matrix[row - i][col - i]
  return product

def topRight(row, col):
  product = 1
  for i in range(4):
    if row - i > 0 and col + i < 20:
      product = product * matrix[row - i][col + i]
  return product

def botLeft(row, col):
  product = 1
  for i in range(4):
    if row + i < 20 and col - i > 0:
      product = product * matrix[row + i][col - i]
  return product

def botRight(row, col):
  product = 1
  for i in range(4):
    if row + i < 20 and col + i < 20:
      product = product * matrix[row + i][col + i]
  return product


funcs = [checkTop, checkBot, checkLeft, checkRight, topLeft, topRight, botLeft, botRight]

product = 1
for i in range(20):
  for j in range(20):
    for k in range(8):
      tmp = funcs[k](i,j)
      if tmp > product:
        product = tmp

print product

# 70600674








