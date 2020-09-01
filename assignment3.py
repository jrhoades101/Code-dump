_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

#Asks the user whether they want to solve for a single or range square roots.
answer = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")

#This if statement will be executed if the user chooses a single integer value.
if answer == 'single' or answer == 'Single':
    value = float(input("Enter a positive integer value: "))
#A list of variables that are being defined, these variables will be used for the Babylonian method.
    epsilon = 0.0001
    x = value
#estimate is set to the lowest possible number, in this case, 1 as inputting anything higher may cause an error in the calculated square root.
    estimate = 1
#The while loop will keep going until the 'estimate' is less than the epsilon.
    while (epsilon < x - estimate):
        x = (estimate + x) / 2
        estimate = value / x
#square_root will output whatever number comes from the estimate to result in our final square root value.
    square_root = estimate
#This while loop will keep repeating until the integer is greater than 0.
    while value < 0:
        print("Error! Please enter an integer that is above 0.")
        value = float(input("Enter a positive integer value: "))
    print("Value     Square Root")
    print(int(value), "       ", format(square_root, ".3f"))


#This elif statement will be executed if the user chooses a range of different integer values.
elif answer == 'range' or answer == 'Range':
    range_start = float(input("Enter a positive integer value to start your range: "))
#This while loop will result in an error message unless the inputed number is above 0.
    while range_start < 0:
        print("Error! Please enter an integer that is above 0.")
        range_start = float(input("Enter a positive integer value to start your range: "))
        range_end = float(input("Enter a positive integer value to end your range: "))
#This while loop will result in an error message unless the inputed number is less than 100.
    while range_end > 100:
        print("Error! Please enter an integer that is above 100.")
        range_start = float(input("Enter a positive integer value to start your range: "))
        range_end = float(input("Enter a positive integer value to end your range: "))
#This while loop will check to see if the starting value is greater than 0 and if the ending number is less than 100.
    while (range_start < 0) or (range_end > 100):
        print("Error! Please enter an integer that is above 0 and less than 100.")
        range_start = float(input("Enter a positive integer value to start your range: "))
        range_end = float(input("Enter a positive integer value to end your range: "))
    loop_start = range_start
    print("Value     Square Root")

    for b in range(int(range_start), int(range_end + 1)):
#A list of variables that are being defined, these variables will be used for the Babylonian method.
        epsilon = 0.0001
        x = loop_start
#estimate is set to the lowest possible number, in this case, 1 as inputting anything higher may cause an error in the calculated square root.
        estimate = 1
#The while loop will keep repeating until the 'estimate' is less than the epsilon.
        while (epsilon < x - estimate):
            x = (x + estimate) / 2
            estimate = loop_start / x
#square_root will output whatever number comes from the estimate to result in our final square root value.
        square_root = estimate
#// I was able to format my text to be right aligned by following the guide from: https://pyformat.info/
        print('{:3d}'.format(int(loop_start)),"        ",format(square_root, ".3f"))
        loop_start += 1


















