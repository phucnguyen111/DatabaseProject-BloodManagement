import psycopg2
from databaseInfo import user, password, host, port, database
'''
This function deletes the blood entry in the Blood database.
NOTE: Practical use in the project is unclear. Need further ìnormation
@param[in]:         bID             Blood's ID

@return:            status          The status of blood record deletion
                    1               Success
                    0               Failure
'''

def deleteBlood(perID, donationDate):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()


        print("Deleting Blood of donor %s with the date %s: ",  (perID, donationDate) )

        sql_delete_query = """delete from Blood where PersonalID = %s and DonationDate = %s"""
        cursor.execute(sql_delete_query, (perID,donationDate))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Blood table...")
        return 1

    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Blood:", error)
        return 0
    # finally:
    #     if(connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")
