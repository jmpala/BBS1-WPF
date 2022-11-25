
def print_menu():
    print("Enter one of the following options")
    print("'insert' - adds a new number")
    print("'print' - prints all the numbers")
    print("'size' - numbers of elements on the list")
    print("'deletepos' - deletes element at given position")
    print("'clearall' - clears all the numbers")
    print("'end' - terminates the program")


numbers = []

while True:
    print_menu()
    inp = input("Insert an option...")
    inp = inp.lower()
    if inp == "end":
        print("Exiting program")
        exit()
    elif inp == "insert":
        new_number = int(input("Insert a number..."))
        numbers.append(new_number)
    elif inp == "print":
        print("numbers: ", numbers)
    elif inp == "size":
        print("Size: ", len(numbers))
    elif inp == "deletepos":
        pos = int(input("Insert position..."))
        try:
            numbers.remove(numbers[pos])
        except IndexError:
            print("Index out of bounds")
    elif inp == "clearall":
        numbers.clear()
        print("Numbers cleared!!!")
    else:
        print("No valid option selected...")

print("Exiting program...")
