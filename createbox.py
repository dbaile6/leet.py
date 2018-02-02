#function that asks user for the number
def get_number_from_user():
    return int(raw_input("How big is the square? "))

#creating rules for how the box should look
def create_a_box(size):
    y = 0
    box = ""
    while y < size:
        x = 0
        row = ""
        y = y + 1
        while x < size:
            x = x + 1
            row = row + " *"
        box = box + row + "\n"
        # print row
    return box

def main():
    # get a number
    box_size = get_number_from_user()

    # create the box, using the number i got from the user
    the_box = create_a_box(box_size)

    # draw the box
    print the_box

main(n)