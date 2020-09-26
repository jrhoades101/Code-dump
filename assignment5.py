_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'

# Grading variables are set for the files, H-F is for GRADS while A-F2 are for UNDERGRAD.
H = range(95, 101)
P = range(80, 95)
L = range(70, 80)
F = range(0, 70)

A = range(90, 101)
B = range(80, 90)
C = range(70, 80)
D = range(60, 70)
F2 = range(0, 60)

# Prompt the user to enter the name of the input file, making sure that the file exists and asking the user to re-enter a filename if needed.
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

# Read the input file, assign grades as appropriate for the type of student (GRAD vs. UNDERGRAD), and write the output to file.
line = input_file.readline()
line = line.rstrip('\n')
while line != '':
    # The file will sort names and grade if 'GRAD' is read.
    if line == 'GRAD':
        line = input_file.readline()
        line = line.rstrip('\n')
        # Prints the name.
        line = output_file.write(line)
        line = input_file.readline()
        line = int(line.rstrip('\n'))
        # Will sort the grade based on the global variables.
        if line in H:
            output_file.write('\nH\n')
        elif line in P:
            output_file.write('\nP\n')
        elif line in L:
            output_file.write('\nL\n')
        elif line in F:
            output_file.write('\nF\n')
    # The file will sort names and grade if 'UNDERGRAD' is read.
    elif line == 'UNDERGRAD':
        line = input_file.readline()
        line = line.rstrip('\n')
        # Prints the name.
        line = output_file.write(line)
        line = input_file.readline()
        line = int(line.rstrip('\n'))
        # Will sort the grade based on the global variables.
        if line in A:
            output_file.write('\nA\n')
        elif line in B:
            output_file.write('\nB\n')
        elif line in C:
            output_file.write('\nC\n')
        elif line in D:
            output_file.write('\nD\n')
        elif line in F2:
            output_file.write('\nF\n')

    # If an error is caught, it will be processed and the program will gently end.
    else:
        print("The program caught an error at")
        print("The correct format for files should include 'GRAD' and 'UNDERGRAD'.")
        print("The files will now close.")
        break
    line = input_file.readline()
    line = line.rstrip('\n')

# The files are being closed after being used.
input_file.close()
output_file.close()

# Gracefully handle errors in the input file. In particular, your program should catch errors such as invalid numbers
# for grades, or student categories that are not "GRAD" or "UNDERGRAD".










