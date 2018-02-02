def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

        return largest

print largest_number([4, 7, 10, 5])