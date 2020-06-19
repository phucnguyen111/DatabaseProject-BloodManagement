import psycopg2
from DBQueriesPython.databaseInfo import user, password, host, port, database
'''
This function updates the amount of blood in the required blood group everytime new blood donation is created and is successful.

@param[in]:     bgBloodType           The type of this blood group
@param[in]:     bgAddedAmount         The amount added to this blood group


@return         status                  Whether the request history is successful or not
                1                       Blood group is successfully added to the table
                0                       Database has error, can not add this record
'''

def addToBloodGroup (bgBloodType, bgAddedAmount):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        cursor.execute("""select TotalAmount from BloodGroup where BloodType = %s""", (bgBloodType,))
        current_amount = cursor.fetchone()[0]
        current_amount += bgAddedAmount

        print("Adding into blood group: ",bgBloodType,"~",bgAddedAmount)
        cursor.execute("""update BloodGroup set TotalAmount = %s where BloodType = %s""", (current_amount, bgBloodType))
        connection.commit()

        count = cursor.rowcount
        print(count, "records sucessfully inserted into BloodGroup table")

        return 1

    except(Exception, psycopg2.Error) as error:
        if(connection):
            print("Error inserting record into BloodGroup table: ", error)
            return 0
    finally:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

