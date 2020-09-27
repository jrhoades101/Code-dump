_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

# Initializes the curve for the grades.
curve_grade = 0
count = 0
name = ""

# Prompts the user to enter the name of a input file, making sure that the file exists and asks the user to re-enter a filename if needed.
first_file = None

while first_file is None:
    try:
        first_file = input("Please enter the name of the input data file: ")
        input_file = open(first_file, 'r')
    # If an error is found it will go through this loop and repeat until a proper file is found.
    except FileNotFoundError:
        print("File does not exist. Please enter a valid input data file.")
        first_file = None

# Prompt the user to enter the name of an output file. The output file should be erased/overwritten if an old one with the same name exists.
second_file = input("Please enter the name of the output data file: ")
output_file = open(second_file, 'w')

# Asks the user if they want to curve grades.
answer = input("Would you like to curve the grades? (Y/N) ")
if answer == 'Y' or answer == 'y':
    curve_grade = int(input("Please enter the score that should map to a '100%' grade: "))
    while curve_grade <= 0:
        print("Invalid curve grade input, please enter grade between 1-100.")
        curve_grade = int(input("Please enter the score that should map to a '100%' grade: "))

# Read the input file, assign grades as appropriate for the type of student (GRAD vs. UNDERGRAD), and write the output to file.
line = input_file.readline()
line = line.rstrip('\n')
while line != '':

    # The file will sort names and grade if 'GRAD' is read.
    if line == 'GRAD':
        # Reads the name
        name = line
        line = input_file.readline()
        line = line.rstrip('\n')

        # Reads the grade.
        line = input_file.readline()
        line = int(line.rstrip('\n'))

        # If statement based on if the user wants to curve the grades.
        if answer == 'Y' or answer == 'y':
            try:
                final_curve = 100 / curve_grade
                line *= final_curve
            except ZeroDivisionError:
                if curve_grade <= 0:
                    print("The curve grade was below 0, try again. ")

        # Will sort the grade based on the appropriate operators.
        if line >= 95:
            output_file.write(name)
            output_file.write('\nH\n')
        elif line >= 80 and line < 95:
            output_file.write(name)
            output_file.write('\nP\n')
        elif line >= 70 and line < 80:
            output_file.write(name)
            output_file.write('\nL\n')
        elif line >= 0 and line < 70:
            output_file.write(name)
            output_file.write('\nF\n')
        else:
            print("Unknown grade detected (" + str(line) + ").")
            print("Error occurred while determining letter grade. Aborting.")
            count += 1
    # The file will sort names and grade if 'UNDERGRAD' is read.
    elif line == 'UNDERGRAD':
        # Reads the name.
        name = line
        line = input_file.readline()
        line = line.rstrip('\n')

        # Reads the grade.        
        line = input_file.readline()
        line = int(line.rstrip('\n'))

        # If statement based on if the user wants to curve the grades.
        if answer == 'Y' or answer == 'y':
            try:
                final_curve = 100 / curve_grade
                line *= final_curve
            except ZeroDivisionError:
                if curve_grade <= 0:
                    print("The curve grade was below 0, try again. ")

        # Will sort the grade based on the appropriate operators.
        if line >= 90:
            output_file.write(name)
            output_file.write('\nA\n')
        elif line >= 80 and line < 90:
            output_file.write(name)
            output_file.write('\nB\n')
        elif line >= 70 and line < 80:
            output_file.write(name)
            output_file.write('\nC\n')
        elif line >= 60 and line < 70:
            output_file.write(name)
            output_file.write('\nD\n')
        elif line >= 0 and line < 60:
            output_file.write(name)
            output_file.write('\nF\n')
        else:
            print("Unknown grade detected (" + str(line) + ").")
            print("Error occurred while determining letter grade. Aborting.")
            count += 1
            
    # If an error is caught, it will be processed and the program will gently end.
    else:
        print("Unknown student category detected (" + str(line) + ").")
        print("Error occurred while determining letter grade. Aborting.")
        input_file.readline()
        input_file.readline()
        count += 1

    # Reads the lines in the files.
    line = input_file.readline()
    line = line.rstrip('\n')

# Confirmation message that the files were processed and saved.
if count == 0:
    print("All data was successfully processed and saved to the requested output file.")

# The files are being closed after being used.
input_file.close()
output_file.close()

# Gracefully handle errors in the input file. In particular, your program should catch errors such as invalid numbers
# for grades, or student categories that are not "GRAD" or "UNDERGRAD".











