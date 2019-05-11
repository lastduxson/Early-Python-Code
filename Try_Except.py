#==============================================================================#
# TITLE: Try_Except
# Script to demonstrate Exception Handling
# AUTHOR: RER
# DATE: 8 May 2019
# ChangeLog (When, Who, What):
# ---- 8 May 2019, RER, Created Script
#==============================================================================#
# 
# Start while loop
again = True
while (again == True):
#
# Ask for input
    print("\nPrepare to ENTER 2 numbers with which to perform")
    print("the four basic arithmetic operations")
#
# Get numbers
    N1 = float(input("Enter the first number, N1 \n"))
    N2 = float(input("Enter the second number, N2 \n"))
#
# Do sum, difference, product, quotient of N1 and N2
    print("\nN1 + N2 = ",N1+N2)
    print("\nN1 - N2 = ",N1-N2)
    print("\nN1 * N2 = ",N1*N2)
#
# Flag zero divide exception
    try:
        print("\nN1/N2 = ",N1/N2)
    except ZeroDivisionError:
        print("\nN1/N2 is indeterminate since N2 = 0")
#
# Ask for a retry
    YorN = input("\nTry again? (Y or N):")
    YorN = YorN.upper()
    if YorN == 'N':
        again = False
#
# All done
print("\nPress ENTER to end this script")
input()




      
