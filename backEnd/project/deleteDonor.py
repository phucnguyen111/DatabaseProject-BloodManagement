import psycopg2

def deleteDonor(donID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()


        print("Deleting donor with the ID: ", donID)

        sql_insert_query = """delete from Donor where DonorID = %s"""
        cursor.execute(sql_insert_query, (donID,))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Donor table...")

    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Donor:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

donID = 1

deleteDonor(1)