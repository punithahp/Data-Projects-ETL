'''
Usecase: In a local gym, every month there is a need to find out the list of members who are currently active and
enrolled for the "Gold", "Silver" and "Bronze" memberships. This will help the gym's marketing team to plan for targeted
promotions of various services offered at the gym to selected group of members.

Problem statement: Currently, someone have to manually evaluate the "current members.txt" file to address the above usecase. It would be great,
if this process can be automated with python program

Note: for illustration purposes of this project, we are going to generate some sample data and then process it to address the usecase listed above.
    Input:
    "MonthlyFile" --> File that contains the list of all members (including active/inactive and all membership categories) at the end of each month.
    Output:
    "GoldMonthlyFile" --> File that contains the list of all members who have "Gold" membership
    "SilverMonthlyFile" --> File that contains the list of all members who have "Silver" membership
    "BronzeMonthlyFile" --> that contains the list of all members who have "Bronze" membership

Author: Punitha Panneerselvam
Date: 5/21/2024
'''

# Need to import this library for data creation needs
from random import randint as rnd

# initializing all the variables
MonthFile = "./data/MonthlyFile.txt"
GldFile = "./data/GoldMonthlyFile.txt"
SlvrFile = "./data/SilverMonthlyFile.txt"
BrnzFile = "./data/BronzeMonthlyFile.txt"
status = ["active", "terminated"]
category = ["Gold", "Silver", "Bronze"]
ID = 0
active_list = []


# The below function is to generate some sample data for the input file for illustration purposes
def CreateFiles(MnthF):
    # opening in w+ mode will create the file if it does not exist. so, used w+ mode to read and write file instead of r+
    with open(MnthF, "w+") as readfile:
        readfile.write("Membership_ID   Join_date   Status   Category \n")
        data = "{:<15} {:<11} {:<8} {:<10} \n"

        # This loop is used to add sample data in a formatted manner into the input file"
        for i in range(100):
            ID = i + 1
            date = str(rnd(2015, 2024)) + '-' + str(rnd(1, 12)) + '-' + str(rnd(1, 31))
            readfile.write(data.format(ID, date, status[rnd(0, 1)], category[rnd(0, 2)]))


'''
The below function will open the input file in "read" mode and all the output files in "write" mode. 
Then the input data is analyzed further to filter out the "active members" into a list
Then from the "active members" list, the "gold", "silver" and "bronze" membership records are filtered out and written into their respective 
monthly file.
'''


def ProcessData(MntF, GldF, SlvrF, BrnzF):
    with open(MntF, "r+") as readfile:
        with open(GldF, "w+") as writegldfile:
            with open(SlvrF, "w+") as writeslvrfile:
                with open(BrnzF, "w+") as writebrnzfile:
                    readfile.seek(0)
                    All_members = readfile.readlines()
                    # print(All_members)
                    Header = All_members[0]
                    All_members.pop(0)

                    for member in All_members:
                        if "active" in member:
                            active_list.append(member)

                    writegldfile.seek(0)
                    writeslvrfile.seek(0)
                    writebrnzfile.seek(0)
                    writegldfile.write(Header)
                    writeslvrfile.write(Header)
                    writebrnzfile.write(Header)
                    for mem in active_list:
                        if "Gold" in mem:
                            writegldfile.write(mem)
                        elif "Silver" in mem:
                            writeslvrfile.write(mem)
                        elif "Bronze" in mem:
                            writebrnzfile.write(mem)
                    writebrnzfile.truncate()
                writeslvrfile.truncate()
            writegldfile.truncate()


def readfiles(filetoread):
    with open(filetoread, 'r') as readfile:
        print(readfile.read())


'''
calling the creatfile function to generate the input file or the "MonthlyFile.txt" that contains all 
the members details (active/terminated, gold/silver/bronze membership categories)
'''
CreateFiles(MonthFile)
print("Newly created monthly file: \n")
# This block is to read the newly generated input file and print it for the user to read
readfiles(MonthFile)

# calling the processdata() function to process the inputfile and produce the desired output files.
ProcessData(MonthFile, GldFile, SlvrFile, BrnzFile)
'''
Finally, the desired output monthly files are created and ready for the user to read. The below block of code is to read data from the 3 output files.
The data in these files can be used for promotional needs as desired by the Gym's marketing team.
'''
print("Newly created Gold monthly file: \n")
readfiles(GldFile)
print("Newly created Silver monthly file: \n")
readfiles(SlvrFile)
print("Newly created Bronze monthly file: \n")
readfiles(BrnzFile)

