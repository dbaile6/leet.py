arrayofnumbers = [
    "0"
    "1"
    "2"
    "3"
    "4"
    "5"
    "6"
    "7"
    "8"
    "9"
    "10"
]

start_number = int(raw_input("Pick a number to start on "))
end_number = int(raw_input("Pick a number to end on "))

i = 0
for i in range(0, len(arrayofnumbers)):
    if start_number < end_number:
        print range(start_number, end_number)
