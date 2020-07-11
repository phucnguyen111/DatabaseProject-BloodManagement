import psycopg2
from calculateMonthDiffDB import calculateMonthDiff
from databaseInfo import user, password, host, port, database
'''
This function is used to add a blood entry to the Blood database.
It first checks whether the donor's last donation was more than 3 months ago. If not then addition of blood is not allowed.

@param[in]  bPerID          Blood personal ID, ID of the blood donor   
@param[in]  bBloodType      Type of blood
@param[in]  bAmount         Amount of blood

@return     status          The status of adding blood to the database
            0               Database error, can not add
            1               Add successfully to the table
            -1              Donor da ton tai va da hien mau trong vong 3 thang tro lai day
            -2              Database error while calculating difference in months in calculateMonthDiff.py
'''


def addBlood(bPerID, bBloodType, bAmount):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        (monthDiff, latest_date) = calculateMonthDiff(bPerID, cursor)
        if(monthDiff >=0 and monthDiff < 3): #Donor da ton tai va da hien mau trong vong 3 thang tro lai day
            print(" --> Last donated was less than 3 months")
            return (-1, latest_date)
        elif(monthDiff == -1 ): #Loi database tron calculateMonthDiff
            print("Error while calculating difference in months --> check calculateMonthDiff")
            return (-2, latest_date)
        else: #Donor chua ton tai hoac Donor da ton tai va hien mau ngoai 3 thang tro lai day
            print("Adding blood: ", bPerID, "~", bBloodType, "~" + str(bAmount))
            sql_insert_query = """insert into Blood(PersonalID, BloodType, Amount, DonationDate) values(%s,%s,%s,NOW())"""
            record_to_insert = (bPerID, bBloodType, bAmount)
            cursor.execute(sql_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            return (1, latest_date)

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into Blood:", error)
            return (0, latest_date)
    # finally:
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")

# bPerID = 112233
# bBloodType = "A+"
# bAmount = 123.5
# addBlood(bPerID,bBloodType,bAmount)
