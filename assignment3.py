_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'


answer = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")


if answer == 'single' or answer == 'Single':
    value = float(input("Enter a positive integer value: "))
    babylonian = value
    b = value
    method = 1
    epsilon = 0.0001
    while (b - method > epsilon):
        b = (b + method) / 2
        method = value / b
    square_root = method
    while value < 0:
        print("Error! Please enter an integer that is above 0.")
        value = float(input("Enter a positive integer value: "))
    print("Value     Square Root")
    print(int(value), "       ", format(square_root, ".3f"))



elif answer == 'range' or answer == 'Range':
    range_start = float(input("Enter a positive integer value to start your range: "))


    while range_start < 0:
        print("Error! Please enter an integer that is above 0.")
        range_start = float(input("Enter a positive integer value to start your range: "))
    range_end = float(input("Enter a positive integer value to end your range: "))
    while range_end > 100:
        print("Error! Please enter an integer that is above 100.")
        range_end = float(input("Enter a positive integer value to end your range: "))
    while (range_start < 0) or (range_end > 100):
        print("Error! Please enter an integer that is above 0 and less than 100.")
        range_start = float(input("Enter a positive integer value to start your range: "))
        range_end = float(input("Enter a positive integer value to end your range: "))
    loop_start = range_start

    print("Value     Square Root")

    for v in range(int(range_start), int(range_end + 1)):
        babylonian = loop_start
        b = loop_start
        method = 1
        epsilon = 0.0001
        while (b - method > epsilon):
            b = (b + method) / 2
            method = loop_start / b
        square_root = method
        print('{:3d}'.format(int(loop_start)),"     ",format(square_root, ".3f"))
        loop_start += 1


















