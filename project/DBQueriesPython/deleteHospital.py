import psycopg2


'''
This function is used to delete a donor. 
@param[in]:     hID                     Hospital's personal ID

@return         status                  Whether deletion is successful or not
                1                       Request history is successfully added to the table
                0                       Database has error, can not add this record
'''

def deleteHopital(hID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="ha3171999",
                                      host="localhost",
                                      port="5432",
                                      database="BloodBank")
        cursor = connection.cursor()


        print("Deleting donor with the ID: ", hID)

        sql_delete_query = """delete from Donor where PersonalID = %s"""
        cursor.execute(sql_delete_query, (hID,))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Donor table...")
        return 1
    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Donor:", error)
        return 0
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

#---------------------------------------------------------------
#Return values:
#1: Deleted from table
#0: Database error -> not deleted