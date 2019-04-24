#==============================================================================#
# TITLE: Script to perform multiplication of a 2x1 vector by a 2x2 matrix
#        PLUS do sum, difference, product and quotient of the vector components
# AUTHOR: RER
# DATE: 4 April 2019
# ChangeLog (When, Who, What):
# ---- 4 April 2019, RER, Created Script
# ---- 10 April 2019, RER, Enhanced Script
#==============================================================================#
#
# Get Matrix Elements
a11 = float(input("Enter the a11 element of a 2x2 matrix, A\n"))
a12 = float(input("Enter the a12 element of the 2x2 matrix, A\n"))
a21 = float(input("Enter the a21 element of the 2x2 matrix, A\n"))
a22 = float(input("Enter the a22 element of the 2x2 matrix, A\n"))
# Get Vector Elements
b1 = float(input("Enter the first element, b1, of a vector, b\n"))
b2 = float(input("Enter the first element, b2, of the vector, b\n"))
print("\nThe first and second elements, c1 and c2,\nof the product c = Ab are:")
# Perform the Multiplication and Display the Results
print("c1 = ", a11*b1 + a12*b2)
print("c2 = ", a21*b1 + a22*b2)
#
# Do sum, difference, product, quotient of b1 and b2
print("\nBTW, FYI:")
print("b1 + b2 = ",b1+b2)
print("b1 - b2 = ",b1-b2)
print("b1 * b2 = ",b1*b2)
if b2 != 0:
    print("b1/b2 = ",b1/b2)
else:
    print("b1/b2 is indeterminate since b2 = 0")
#
# All done
print("\nPress ENTER to end this script")
input()




      
