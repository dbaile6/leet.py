numbers = (10, 9, 8, -1, -2)

#def sum(numbers):
#    total = 0
#    for number in numbers:
#        total += number

#    return total

#print sum(numbers)

def positive(numbers):
    for number in numbers:
        if number > 0:
            print number
        else:
            print ' '

print positive(numbers)

#Multiply a List

#factor = 3

#multiplied = []
#for number in numbers:
#    if number > 0:
#        multiplied.append(number * factor)

factor = 3

def multiplied(numbers):
    multiplied = []
    for number in numbers:
        if number > 0:
            multiplied.append(number * factor)

print multiplied(numbers)