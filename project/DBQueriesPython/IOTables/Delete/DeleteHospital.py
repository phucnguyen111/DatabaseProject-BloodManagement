import psycopg2

def deleteHópital(hID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
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