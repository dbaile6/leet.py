numbers = [-5, 4, 7, 10, 5]

#sum = 0
#for number in numbers:
 #   sum += number

  #  print sum
   # 


#largest number

#largest = numbers[0]
#for number in numbers:
#    if number > largest:
#        largest = number

#print largest

# Smallest Number

#smallest = numbers[0]
#for number in numbers:
#    if number < smallest:
#        smallest = number

#print smallest

# Even Numbers

#for number in numbers:
#    if number % 2 == 0:
#        print number

# positive numbers

for number in numbers:
    if number > 0:
        print number

# negative numbers

#for number in numbers:
#    if number < 0:
#        print number

# Multiply a List

#factor = 3

#multiplied = []
#for number in numbers:
#    if number > 0:
#        multiplied.append(number * factor)

# multiply vectors

#vector1 = [1, 4, 7, 9, 8, 4, 1, 2, 3, 4, 5]
#vector2 = [2, 3, -3, 9, 4, 3, 2, 1, 5, 5, 5]

#multiplied = []
#for i in range(0, 5):
#    print i
#    multiplied.append (vector1[i] * vector2[i])

#print multiplied

# matrix addition

matrix1 = [[2,-2], [5,3]]
matrix2 = [[5,2], [1,0]]

height = len(matrix1)
width = len(matrix1[0])

result = []

for i in range(height):
    result.append([])
    for j in range(width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]

        cell = cell1 + cell2

        result[i].append(cell)

print result

# initialize the resulting matrix
for i in range (o, height):
    result.append([])
    for j in range (0, width):
        result.append (None)

# fill in in the matrix
for i in range(0, height):
    result.append([])
    for j in range(0, width):
        result[i].append(None)

def sum:
    total = 0
    for number in numbers:
        total =+ number

print sum([5, 9, 13])