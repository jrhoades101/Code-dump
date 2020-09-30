_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

# A set of variables that are being initialized.
curve_grade = 0
count = 0
name = ""
grade = ""
invalid_input = 0

# Prompts the user to enter the name of a input file, it checks to see if the file exists and asks the user to re-enter a filename if it does not.
first_file = None

while first_file is None:
    try:
        first_file = input("Please enter the name of the input data file: ")
        input_file = open(first_file, 'r')

    # If an error is found it will go through this loop and repeat until a proper file is found.
    except FileNotFoundError:
        print("File does not exist. Please enter a valid input data file.")
        first_file = None

# Prompts the user to enter the name of an output file. The output file will be overwritten if one with the same name exists.
second_file = input("Please enter the name of the output data file: ")
output_file = open(second_file, 'w')

# Asks the user if they want to curve grades.
answer = input("Would you like to curve the grades? (Y/N) ")
if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
    invalid_input += 1

# Repeatedly asks user if they would like to curve the grade if Y or N are not entered.
while invalid_input == 0:
    invalid_input = 0
    print("Invalid input detected. Please enter Y or N.")
    answer = input("Would you like to curve the grades? (Y/N) ")
    if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
        invalid_input += 1

# If statement that is triggered if the user does want to curve the grades.
if answer == 'Y' or answer == 'y':
    while curve_grade == 0:
        try:
            curve_grade = int(input("Please enter the score that should map to a '100%' grade: "))
            while curve_grade <= 0 or curve_grade > 100:
                print("Invalid curve grade input, please enter grade between 1-100.")
                curve_grade = int(input("Please enter the score that should map to a '100%' grade: "))
        except ValueError:
            print("Please only enter numbers between 1-100 for the curved grade.")
            curve_grade = 0



# Reads the input file, assign grades as appropriate for the type of student (GRAD vs. UNDERGRAD), and writes the output to the file.
line = input_file.readline()
line = line.rstrip('\n')
while line != '':

    # The file will sort names and grade if 'GRAD' is read.
    if line == 'GRAD':

        # Reads the name
        line = input_file.readline()
        line = line.rstrip('\n')
        name = line

        # Reads the grade.
        try:
            line = input_file.readline()
            line = int(line.rstrip('\n'))
        except ValueError:
            grade = line.rstrip('\n')
            print("Unknown grade detected (" + grade + ").")
            input_file.close()
            line = ''
            count += 1

        # If statement based on if the user wants to curve the grades.
        if answer == 'Y' or answer == 'y':
            try:
                final_curve = 100 / curve_grade
                line *= final_curve
            except ZeroDivisionError:
                if curve_grade <= 0:
                    print("The curve grade was below 0, try again. ")
            except TypeError:
                    count += 1

        # Will sort the grade based on the appropriate range.
        try:
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
                print("Error occurred while determining letter grade.")
                input_file.close()
                line = ''
                count += 1
        except TypeError:
            print("Error occurred while determining letter grade.")
            count += 1

    # The file will sort names and grade if 'UNDERGRAD' is read.
    elif line == 'UNDERGRAD':

        # Reads the name.
        line = input_file.readline()
        line = line.rstrip('\n')
        name = line

        # Reads the grade.
        try:
            line = input_file.readline()
            line = int(line.rstrip('\n'))
        except ValueError:
            grade = line.rstrip('\n')
            print("Unknown grade detected (" + grade + ").")
            input_file.close()
            line = ''
            count += 1

        # If statement based on if the user wants to curve the grades.
        if answer == 'Y' or answer == 'y':
            try:
                final_curve = 100 / curve_grade
                line *= final_curve
            except ZeroDivisionError:
                if curve_grade <= 0:
                    print("The curve grade was below 0, try again. ")
            except TypeError:
                count += 1

        # Will sort the grade based on the appropriate range.
        try:
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
                print("Error occurred while determining letter grade.")
                input_file.close()
                line = ''
                count += 1
        except TypeError:
            print("Error occurred while determining letter grade.")
            count += 1

    # If an error is caught, the error will be shown and the file will close, gently ending the program.
    else:
        try:
            print("Unknown student category detected (" + str(line) + ").")
            print("Error occurred while determining the name.")
            input_file.close()
            count += 1
        except ValueError:
            print("Error occurred while determining letter grade.")
            count += 1

    # Reads the lines in the files.
    try:
        line = input_file.readline()
        line = line.rstrip('\n')
    except ValueError:

        # Ends the while loop if a ValueError is found.
        print("Please retry the program. Now Aborting.")
        line = ''

# Confirmation message that the files were processed and saved if everything goes smoothly.
if count == 0:
    print("All data was successfully processed and saved to the requested output file.")

# The files are being closed after being used.
input_file.close()
output_file.close()













