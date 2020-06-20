import psycopg2

def deleteDonor(donPerID):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "NVHplay.99.02.21",
                                      host = "localhost",
                                      port = "9221",
                                      database = "BloodDonateProject")
        cursor = connection.cursor()


        print("Deleting donor with the ID: ", donPerID)

        sql_delete_query = """delete from Donor where PersonalID = %s"""
        cursor.execute(sql_delete_query, (donPerID,))
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

deleteDonor(1199232319)