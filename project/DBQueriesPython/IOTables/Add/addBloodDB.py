import psycopg2
from project.DBQueriesPython.AppFunctions.calculateMonthDiff import calculateMonthDiff

def addBlood(bPerID, bBloodType, bAmount): #bDonationDate de la NOW(), bID de la SERIAL
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()

        if(calculateMonthDiff(bPerID) < 3):
            print("This donor has donated less than 3 months ago. Not allowed!")
            return 2
        else:
            print("Adding blood: ", bPerID, "~", bBloodType, "~" + str(bAmount))
            sql_insert_query = """insert into Blood(PersonalID, BloodType, Amount, DonationDate) values(%s,%s,%s,NOW())"""
            record_to_insert = (bPerID, bBloodType, bAmount)
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()

            count = cursor.rowcount
            print(count, "records successfully inserted into Blood table...")
            return 1

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into Blood:", error)
            return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

bPerID = 123456
bBloodType = "A+"
bAmount = 0.5
addBlood(bPerID, bBloodType, bAmount)

#---------------------------------------------------------------
#Return values:
#2: Donated less than 3 months -> not added into table
#1: Added into table
#0: Database error -> not added