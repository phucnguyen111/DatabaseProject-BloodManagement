import psycopg2

def deleteBlood(bID):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="01689240658",
                                      host="localhost",
                                      port="5432",
                                      database="BloodWork")
        cursor = connection.cursor()


        print("Deleting Blood with the ID: ", bID)

        sql_delete_query = """delete from Blood where BloodID = %s"""
        cursor.execute(sql_delete_query, (bID,))
        connection.commit()
        count = cursor.rowcount
        print(count, "records successfully deleted from Blood table...")

    except (Exception, psycopg2.Error) as error:
        print("Error deleting record from Blood:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

