import psycopg2
from calculateMonthDiff import calculateMonthDiff


'''
This function is used to add a blood entry to the Blood database.
It first checks whether the donor's last donation was more than 3 months ago. If not then addition of blood is not allowed.

@param[in]  bPerID          Blood personal ID, ID of the blood donor   
@param[in]  bBloodType      Type of blood
@param[in]  bAmount         Amount of blood

@return     status          The status of adding blood to the database
            0               Database error, can not add
            1               Add successfully to the table
            2               Donor last donated was less than 3 months ago, cannot add this blood to table
'''
def addBlood(bPerID, bBloodType, bAmount): #bDonationDate de la NOW(), bID de la SERIAL
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
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
