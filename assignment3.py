_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

#Asks the user whether they want to select a single or range of integers and their square roots.
answer = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")

#This if statement will be executed if the user chooses a single integer value.
if answer == 'single' or answer == 'Single':
    value = float(input("Enter a positive integer value: "))
#The Babylonian method is executed through a series of variables and mathematical equations.
    babylonian = value
    b = value
    method = 1
    epsilon = 0.0001
#The while loop will keep going until the value is less than the epsilon.
    while (b - method > epsilon):
        b = (b + method) / 2
        method = value / b
    square_root = method
#This while loop will keep repeating until the integer is greater than 0.
    while value < 0:
        print("Error! Please enter an integer that is above 0.")
        value = float(input("Enter a positive integer value: "))
    print("Value     Square Root")
    print(int(value), "       ", format(square_root, ".3f"))


#This elif statement will be executed if the user chooses a range of different integer values.
elif answer == 'range' or answer == 'Range':
    range_start = float(input("Enter a positive integer value to start your range: "))
#I used several while loops to check the user's inputed number. If the inputed number is above 0 then the program proceeds, if it does
# not meet the requirements, it will result in an error.
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
#I used the same Babylonian method as in the if statement, I just replaced the variables to fit the elif statement.
        babylonian = loop_start
        b = loop_start
        method = 1
        epsilon = 0.0001
#The while loop will keep repeating until the value is less than the epsilon.
        while (b - method > epsilon):
            b = (b + method) / 2
            method = loop_start / b
#square_root will register whatever number comes from method to result in our final value.
        square_root = method
#// I was able to format my text to be right aligned by following the guide listed at https://pyformat.info/
        print('{:3d}'.format(int(loop_start)),"     ",format(square_root, ".3f"))
        loop_start += 1


















