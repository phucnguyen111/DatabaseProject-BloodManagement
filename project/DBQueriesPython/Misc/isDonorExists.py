import psycopg2

def isDonorExists(donPerID):
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "01689240658",
                                      host = "localhost",
                                      port = "5432",
                                      database = "BloodWork")

        cursor = connection.cursor()

        sql_select_query = """select * from Donor where PersonalID = %s"""
        cursor.execute(sql_select_query, (donPerID,))
        #data = cursor.fetchall()

        data = cursor.fetchone() #khong can dung den fetchall vi chi kiem tra co ton tai hay k

        #print(data)
        if not data:
            print("Donor", donPerID, "does not exist!")
            return 0
        else:
            print("Donor", donPerID, "existed!")
            return 1

    except (Exception, psycopg2.Error) as error:
        print("Error while checking if the donor ever donated", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

isDonorExists(119923231)
isDonorExists(123456)