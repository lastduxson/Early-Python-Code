#==============================================================================#
# TITLE: HomeInventory
# Script to ask for and write to a text file called SaveIt_or_DumpIt,
# household items and their estimated values to be evaluated for keeping 
# or ditching
#
# AUTHOR: RER
# DATE: 21 April 2019
# ChangeLog (When, Who, What):
# ---- 21 April 2019, RER, Created Script
#==============================================================================#
#
# request household items and estimated values
#
print("""

      You need to downsize. In order to help you decide what household items
      to keep and what to get rid of, you now have the opportunity to create
      a collection of household items and their estimated values.
      
      If you wish, your collection can be saved in a text file called
      SaveIt_or_DumpIt.
      
      """)
#      
input("Press ENTER to get started\n")
#
# obtain household items and approximate values
#
# initialize while loop
#
done = False
#
# obtain household items in while loop
#
n_item = 0
while done == False:
    n_item = n_item+1
    item = input("Enter item: ")
    if n_item == 1:
        item_sav = [item]
    else:
        item_sav.append(item)       
        
    value = input("Enter estimated value of item: ")
    if n_item == 1:
        value_sav = [value]
    else:
        value_sav.append(value)
                
    preference = input("if finished entering items enter DONE, otherwise press ENTER to continue\n")
    if preference != 'DONE':
        continue
    else:
        done = True 
#    
# no further household items
# print list
#
print("\n\nBelow is a list of your items with their estimated values:\n")
for i in range(0, n_item):
    print(item_sav[i],value_sav[i])
#
# ask if text file is desired
#
YES = 'NO'
print("\nWould you like your list to be saved to a text file named 'SaveIt_or_DumpIt'?\n")
YES = input("ENTER 'YES' to save list, or Press ENTER to skip the save\n")
if YES == 'YES':    
    outfile = open("SaveIt_or_DumpIt.txt",'w')
    outfile.write("\n\nList of household items and approximate values is as follows:\n\n")
    for i in range(0,n_item):    
        outfile.write("item = %s, estimated value = $%s\n" %(item_sav[i],value_sav[i]))
#
if YES == 'YES':
    print("\nItem list saved to the file SaveIt_or_DumpIt\n")
    outfile.close()
#   
# end script
input("\n\nPress ENTER to end this script")