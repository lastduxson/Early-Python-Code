#==============================================================================#
# TITLE: What_ToDo
# Script to manage a collection of household tasks and their priorities.
# A list of management options is as follows:
#
# Menu of Options
#    1) Show current data
#    2) Add a new item.
#    3) Remove an existing item.
#    4) Save Data to File
#    5) Exit Program
#
# AUTHOR: RER
# DATE: 28 April 2019
# ChangeLog (When, Who, What):
# ---- 28 April 2019, RER, Created Script
#==============================================================================#
#
#Load Data from the file ToDo.txt
infile = open('ToDo.txt','r')
# Read and display file header
line = infile.readline()
print("\nHeader for file ToDo.txt:")
print(line)
# Load data from file
list = []
nline = 0
while line != '':
    line = infile.readline()
    if line == '':
        continue
    nline = nline + 1
    newline = line.replace('\n','')    
    newline = newline.split(',')
    dict = { newline[0] : newline[1] }
    list.append(dict)
#
# Display a menu of actions
print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
#
while (True):
# choose an option
    strChoice = str(input("\nWhich option would you like to perform? [1 to 5] - "))
# Show the current items in the table
    if (strChoice.strip() == '1'):
        # print data
        print("\nContents of the list (in dictionary form) are as folllows:")
        for i in range(0,nline):
            print("task#",i,list[i])
        continue
# Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        new_task,new_priority = input("Enter new task, priority: ").split(',')
        new_dict = {new_task : new_priority}
        list.append(new_dict)
        print("\nRevised list of tasks is as folllows:")
        nline = nline + 1
        for i in range(0,nline):
            print("task#",i,list[i])    
        continue
# Remove an item from the list/Table
    elif(strChoice == '3'):
        del_index = input("Enter the number of the task to be removed: ")
        del list[int(del_index)]
        print("\nRevised list of tasks is as folllows:")
        nline = nline - 1
        for i in range(0,nline):
            print("task#",i,list[i])
        continue
# Save tasks to a file named RevisedToDo.txt
    elif(strChoice == '4'):
        outfile = open("RevisedToDo.txt",'w')
        outfile.write("This file contains a TODO list, each line in the form: TASK, PRIORITY\n")
        for i in range(0,nline):
            dict = list[i]
            for k,v in dict.items():
                key = k
                value = v
            outfile.write("%s,%s\n" %(key,value))
        print("\nRevised list is saved in a file named RevisedToDo.txt")
        outfile.close()
        continue
# Terminate file actions
    elif (strChoice == '5'):
        print("\nSession is ended")
        break #and end the script

input('\nPress ENTER to end script')


