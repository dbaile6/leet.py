def main():
    # variables width and height
    width = 0
    height = 0

    # Takes input from user for variables
    width = int(input("Please enter the width: "))
    height = int(input("Please enter the height: "))

    i = 0
    max_num = width * height
    while i < max_num:
        i += 1
        needed_space = len(str(max_num)) - len(str(i))
        print(i, " " * needed_space, end='')
        if i % width == 0:
            print("")


ma