import psycopg2

from databaseInfo import user, password, host, port, database

def getBloodAmount(bloodType):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()

        cursor.execute("""select TotalAmount from BloodGroup where BloodType = '{0}'""".format(bloodType))
        print('---executed')
        amount = cursor.fetchone()[0]
        return amount*1000

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Error extracting statistics", error)
    # finally:
    #     if (connection):
    #         cursor.close()
    #         connection.close()
    #         print("PostgreSQL connection is closed")