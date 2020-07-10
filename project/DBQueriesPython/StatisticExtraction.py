import psycopg2

from DBQueriesPython.databaseInfo import user, password, host, port, database

def StatisticExtraction (bloodType):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        cursor.execute("""select TotalAmount from BloodGroup where BloodType = (%s,)""", bloodType)
        amount = cursor.fetchone()[0]
        return amount

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Error inserting record into Blood:", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
