#==============================================================================#
# TITLE: AC_Pickle
# Script to demonstrate Pickling
# AUTHOR: RER
# DATE: 8 May 2019
# ChangeLog (When, Who, What):
# ---- 8 May 2019, RER, Created Script
#==============================================================================#
# 
print("\nThis app provides specs for four Boeing aircraft")
#
import pickle
#
# define Aircraft Specs: type, span(m), MLW(kg/1000)
AC_Specs = [{'B747':['68.5','312.1']}, \
            {'B767':['47.6','136.1']}, \
            {'B777':['60.9','208.7']}, \
            {'B787':['60','172.4']}]
#
# Dump the AC_Specs list to a binary file
ac_pickle = open("AC.dat","ab")
pickle.dump(AC_Specs,ac_pickle)
ac_pickle.close()
#
# Start while loop
again = True
while (again == True):
#
# Choose aircraft for which specs are desired
    AC_in = input("Choose an aircraft from B747, B767, B777, B787:\n")
#
# Test for inclusion in (B747, B767, B777, B787)
    if AC_in not in [ 'B747', 'B767', 'B777', 'B787']:
        print("Choose another aircraft")
        continue
#
# Retrieve AC Specs
    ac_pickle = open("AC.dat","rb")
    AC_Specs = pickle.load(ac_pickle)
    ac_pickle.close()
#
# Obtain specs for desired aircraft and print
    for i in range(0,len(AC_Specs)):
        value = AC_Specs[i].get(AC_in)
        if value != None:
            print("\nFor aircraft of interest " + AC_in  + "\n"  \
            "Wing Span (m) is " + value[0] + "\n"  \
            "Max Landing Weight (kg/1000) is " + value[1])
#
# Ask for aditional specs
    YorN = input("\nInterested in specs for any other aircraft? (Y or N):")
    YorN = YorN.upper()
    if YorN == 'N':
        again = False
#
# All done
input("\nPress ENTER to end this script")