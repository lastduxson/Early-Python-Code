#==============================================================================#
# TITLE: SubmitAuctionItems
# A script to ask for and write to a text file called AuctionItems,
# items to be contributed to a scholarship auction
#
# AUTHOR: RER
# DATE: 13 April 2019
# ChangeLog (When, Who, What):
# ---- 13 April 2019, RER, Created Script
#==============================================================================#
#
# request auction items
#
print("""

      In order to support fund raising to provide 
      financial aid to Python Certificate students,
      please indicate what items you can contribute
      to the upcoming auction and what should be the
      minimum bid.

      Your contributions will be listed in a text file called AuctionItems.

      """)
input("Press ENTER to get started\n\n")
#
# open output file
#
outfile = open("AuctionItems.txt",'w')
outfile.write("\n\nList of auction items and minimum bids is as follows:\n\n")
#
# obtain auction items and minimum bids
#
# initialize for while loop
#
done = False
#
# obtain auction items in while loop
#
while done == False:
    item = input("Enter item (only first 20 characters will be printed): ")
    bid = input("Enter dollar amount of minimum bid: ")
    outfile.write("item = %20s \t minimum bid = $%s\n" %(item[0:20], bid))
    preference = input("if finished entering items enter DONE, otherwise press ENTER to continue\n")
    if preference != 'DONE':
        continue
    else:
        done = True
#    
# no further auction items, close output file
outfile.close()
#
# end script
print("\nPress ENTER to end this script")
input()


      
