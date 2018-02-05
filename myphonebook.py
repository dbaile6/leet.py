def print_menu():
    print('1. Look up a number')
    print('2. Set an entry')
    print('3. Remove a Phone Number')
    print('4. List all entries')
    print('5. Quit')

numbers = {'Dylan': '123-6512',
'Jen': '651-1025'
}

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers")
        name = raw_input("Name: ")
        if name in numbers:
            print("The number is", numbers.get(name))
        else:
            print(name, "was not found")
    elif menu_choice == 2:
        print("Add Name and Number")
        name = raw_input("Name: ")
        phone = raw_input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = raw_input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print numbers
        print()
    elif menu_choice != 5:
        print_menu()