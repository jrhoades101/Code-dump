_author_ = 'Joshua Rhoades, jrhoades@email.unc.edu, Onyen = jrhoades'




print("Enjoy the free use of this Compound Interest Calculator!")
print("-----------------------------------")

#P is the initial amount of the investment (the original principal)
Investment_amount = float(input('Please enter the amount you want to invest: '))
#r is the interest rate
Interest_rate = float(input('Please enter the interest rate: '))
#n is the number of compoundings per year
Compoundings_year = float(input('Please enter the amount of compounds you want per year: '))
#t is the number of years of internet
Years_of_interest = float(input('Please enter the amount of years for the investment: '))

#// This formula was provided through the assignment page. I was able to find the operators through https://www.tutorialspoint.com/python/python_basic_operators.htm
Compound_Interest = (Investment_amount * (1 + (Interest_rate / Compoundings_year)) ** (Years_of_interest * Compoundings_year))

#// Through simple math I was able to figure out the Interest earned and Total balance
Final_Balance = (Compound_Interest + Investment_amount)
Interest_earned = (Compound_Interest - Investment_amount)

#// I used the format code chart from the link below to help myself. I also played around with multiple variations of ",.2f" to get the proper result for the decimal and comma values.
#// https://thepythonguru.com/python-string-formatting/
#I display what the original investment was and then show the amount of interested earned and what the final balance was.
print("Original Investment: $" + format(Investment_amount, ",.2f"))
print("Interested Earned: $" +format(Interest_earned, ",.2f" ))
print("Final Balance: $" +format(Compound_Interest, ",.2f"))
print("-----------------------------------")
print("-----------------------------------")



#// I used https://stackoverflow.com/questions/17953940/yes-or-no-output-python to help base the structure of this If/Elif statement and used a lecture powerpoint to figure out the rest.
answer = (input("Would you like to get a second interest evaluation? "))
if answer == 'yes' or answer == 'Yes':
    Investment_amount1 = float(input('Please enter the amount you want to invest: '))
    Interest_rate1 = float(input('Please enter the interest rate:'))
    Compoundings_year1 = float(input('Please enter the amount of compounds you want per year: '))
    Years_of_interest1 = float(input('Please enter the amount of years for the investment: '))
    Compound_Interest1 = (Investment_amount1 * (1 + (Interest_rate1 / Compoundings_year1)) ** (Years_of_interest1 * Compoundings_year1))
    Final_Balance1 = (Compound_Interest1 + Investment_amount1)
    Interest_earned1 = (Compound_Interest1 - Investment_amount1)
    print("Original Investment: $" + format(Investment_amount1, ",.2f"))
    print("Interested Earned: $" +format(Interest_earned1, ",.2f" ))
    print("Final Balance: $" +format(Compound_Interest1, ",.2f"))
    print("-----------------------------------")
    print("-----------------------------------")
    Compare_Investment = input("Would you like to compare the first investment to the second? ")
    if Compare_Investment == 'yes' or Compare_Investment == 'Yes':
        if Compound_Interest1 >= Compound_Interest:
            print("The second option will result in a larger account balance.")
        elif Compound_Interest1 <= Compound_Interest:
            print("The first option will result in the larger final account balance.")
    elif Compare_Investment == 'no' or Compare_Investment == 'No':
        print("Thank you for getting a second interest evaluation!")
elif answer == 'no' or answer == 'No':
    print("Thank you for using the Compound Investment Calculator!")



