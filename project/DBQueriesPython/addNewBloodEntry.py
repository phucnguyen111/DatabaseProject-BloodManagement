'''
NOTE:   Currently not used at all ?
'''
import psycopg2

from DBQueriesPython.addDonorDB import addDonor
from DBQueriesPython.addBloodDB import addBlood
from DBQueriesPython.calculateMonthDiffDB import calculateMonthDiff
from DBQueriesPython.addDonateDB import addDonate
'''
This function is to create a new blood entry whenever a donor register a blood donation. 
Change password, database according to your database
NOTE: need to return query status: 
+ Successful: 1
+ User's last donation is too close to current register: -1
'''

def addNewBloodEntry(donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont, bID, bAmount, bStatus):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
        cursor = connection.cursor()
        # tim xem donor da ton tai chua
        sql_find_donor_query = """select * from Donor where PersonalID = %s"""
        cursor.execute(sql_find_donor_query, (donPerID,))
        isFound = cursor.fetchone()
        print("Found donor: ",isFound)

        if isFound:
            data = calculateMonthDiff(donPerID)
            if (data < 3):
                print("This donor has just donated less than 3 months ago and is not allowed to donate again this time!")
                return
            else:
                print("Permission to donate")
                addDonor(donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont)
                addBlood(bID, bAmount, bStatus)
                addDonate(donDonID, bID)
        else:
            print("Not Found")
            addDonor(donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont)
            addBlood(bID, bAmount, bStatus)
            addDonate(donDonID, bID)

    except (Exception, psycopg2.Error) as error:
        print("Error inserting record to Donor, Blood & Donate:", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


donDonID = "123457_160520"
donPerID = 123457
donName = "John Haston"
donGender = "Male"
donAddress = "Paris"
donEmail = "John_DeGraf1778@gmail.com"
donCont = "ND1QNWQ927WD"
bID = "123457_160520"
bAmount = 200
bStatus = "Healthy"

addNewBloodEntry(donDonID, donPerID, donName, donGender, donAddress, donEmail, donCont, bID, bAmount, bStatus)
