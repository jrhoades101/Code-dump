_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

answer = input(" Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")



if answer == 'single' or answer == 'Single':
    value = float(input("Enter a positive integer value: "))
    while value < 0:
        print("Error! Please enter an integer that is above 0.")
        value = float(input("Enter a positive integer value: "))
    square_root = float(value**(1 / 2))
    print("Value     Square Root")
    print(value,"       ", format(square_root, ".3f"))


elif answer == 'range' or answer == 'Range':
    range_start = float(input("Enter a positive integer value to start your range: "))
    range_end = float(input("Enter a positive integer value to end your range: "))
    while (range_start < 0) or (range_start > 100):
        print("Error! Please enter an integer that is above 0 and less than 100.")
        range_start = float(input("Enter a positive integer value to start your range: "))
        range_end = float(input("Enter a positive integer value to end your range: "))
    square_root = float(range_start**(1 / 2)) and float(range_start**(1 / 2))
    print("Value     Square Root")
    print(range_start,"       ", square_root)
