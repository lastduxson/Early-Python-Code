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
      SaveIt_or_DumpIt-TupleVersion.
      
      """)
#      
input("Press ENTER to get started\n")
#
# obtain household items and approximate values
#
# open output file
#
outfile = open("SaveIt_or_DumpIt-TupleVersion.txt",'w')
outfile.write("\n\nList of household items and approximate values is as follows:\n\n")
#
# initialize while loop
#
done = False
#
# obtain household items in while loop
#
while done == False:
    item = input("Enter item: ")   
    value = input("Enter estimated value of item: ")
#
# form tuple
    item_value = (item,value)
#
    outfile.write("item = %s, estimated value = $%s\n" %(item_value[0],item_value[1]))
#                
    preference = input("if finished entering items enter DONE, otherwise press ENTER to continue\n")
    if preference != 'DONE':
        continue
    else:
        done = True 
#    
# no further household items
# ask if text file is desired
#
YES = 'NO'
print("\nWould you like your list to be saved to a text file named 'SaveIt_or_DumpIt'?\n")
YES = input("ENTER 'YES' to save list, or Press ENTER to skip the save\n")
if YES != 'YES':    
    outfile.truncate(0)

outfile.close()
#   
# end script
input("\n\nPress ENTER to end this script")
